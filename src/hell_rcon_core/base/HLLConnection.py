#!/usr/bin/env python
# -*-coding:utf-8 -*-
import array
import re
import socket
import sys
import time
import uuid
from threading import get_ident
from typing import List, Any

from .HLLBaseConnection import HLLBaseConnection
from .HLLBaseException import HLLAuthError, HLLServerError
from .HLLBaseLogging import get_logger

"""
  默认的 socket 读写长度 32KB, 最大为 64KB
  实际 HLL 的socket读写长度为8KB
"""
MSGLEN = 8 * 1024
SOCKET_TIMEOUT_SEC = 10

logger = get_logger(__name__)


class HLLConnection(HLLBaseConnection):
    def __init__(self, host: str | None = None, port: str | None = None, password: str | None = None) -> None:
        """
        初始化连接
        self.xorkey: 一个用于XOR运算的密钥，初始为None，可能在后续用于数据的加解密
        self.sock: 一个IPv4的流式socket

        self.id: 一个基于线程标识符和随机UUID的唯一ID
        """
        self.xorkey = None
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.settimeout(SOCKET_TIMEOUT_SEC)
        # 设置 TCP 心跳
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, True)
        if sys.platform == "win32":
            self.sock.ioctl(socket.SIO_KEEPALIVE_VALS, (1, 60 * 1000, 30 * 1000))
        else:
            # linux 系统
            self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)  # 开启
            self.sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPIDLE, 60)  # 60s
            self.sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPINTVL, 30)
            self.sock.setsockopt(socket.SOL_TCP, socket.TCP_KEEPCNT, 3)

        self.id = f"{get_ident()}-{uuid.uuid4()}"
        if host and port and password:
            self.connect(host, port, password)

    def connect(self, host: str, port: str, password: str):
        self.sock.connect((host, int(port)))
        self.xorkey = self.sock.recv(MSGLEN)
        result = self.get_request(f"Login {password}")
        if result != "SUCCESS":
            raise HLLAuthError("Invalid password")
        logger.info(f"登录成功")
        # recv_buff = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_RCVBUF)
        # send_buff = self.sock.getsockopt(socket.SOL_SOCKET, socket.SO_SNDBUF)
        # print(f'默认接收缓冲区大小：{recv_buff}。默认发送缓冲区大小：{send_buff}')

    def close(self) -> None:
        try:
            self.sock.shutdown(socket.SHUT_RDWR)
        except OSError:
            logger.debug("Unable to send socket shutdown")
        self.sock.close()

    def send(self, msg) -> int:
        """编码发送"""
        xored = self._xor(msg.encode())
        sent = self.sock.send(xored)
        # if sent != len(msg):
        #     raise RuntimeError("socket connection broken")
        return sent

    def _xor(self, msg) -> bytes:
        """编码解码"""
        n = []
        if not self.xorkey:
            raise RuntimeError("The game server did not return a key")
        for i in range(len(msg)):
            n.append(msg[i] ^ self.xorkey[i % len(self.xorkey)])
        return array.array("B", n).tobytes()

    def receive(self, msglen=MSGLEN) -> str:
        """接收数据并整合解码"""
        buff = self.sock.recv(msglen)
        msg = self._xor(buff)
        while len(buff) >= msglen:
            try:
                buff = self.sock.recv(msglen)
            except socket.timeout:
                break
            msg += self._xor(buff)

        # if not msg.endswith(b'\n'):
        #     msg = msg.rsplit(b'\n')[0]
        try:
            return msg.decode()
        except UnicodeDecodeError:
            return msg.decode(errors='ignore')

    def get_request(self, command: str, is_list=False, log_info=False) -> str | list[Any]:
        """RCON 指令"""
        self.send(command)
        time.sleep(0.1)

        if re.match(r'^login', command, re.I):
            command = "login ********"
        if log_info:
            logger.info(f"> {command}")
        else:
            logger.debug(f"> {command}")

        raw = self.receive()
        if not is_list:
            return raw
        else:
            res = raw.split("\t")
            try:
                expected_len = int(res.pop(0))
                logger.debug(f"获取列表长度 {expected_len}")
            except ValueError:
                raise HLLServerError("来自服务器的意外响应。" "无法获取列表长度")

            res = [i for i in res if i]
            if expected_len < len(res):
                raise HLLServerError(
                    "服务器返回不完整列表,"
                    f" 预计 {expected_len} 但获取 {len(res)}"
                )

            return res
