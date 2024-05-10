#!/usr/bin/env python
# -*-coding:utf-8 -*-
from .HLLBaseException import HLLAuthError


class HLLBaseConnection:

    def connect(self, host: str, port: str, password: str) -> None: pass
    def close(self) -> None: pass
    def send(self, msg) -> int: pass
    def _xor(self, msg) -> bytes: pass
    def receive(self, msglen) -> str: pass
    def __enter__(self): return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        self.close()
        if exc_type is not None:
            raise HLLAuthError("Connection Error")