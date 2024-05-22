#!/usr/bin/env python
# -*-coding:utf-8 -*-
import re
import time
from functools import wraps
from typing import Any, Dict, List

from .base.HLLBaseLogging import get_logger
from .base.HLLCommands import HLLCommands

logger = get_logger(__name__)


def call_parent_first(func):
    @wraps(func)
    def wrapper(child_self, *args, **kwargs):
        # 获取父类的方法
        parent_class = type(child_self).mro()[1]
        parent_method = getattr(parent_class, func.__name__)
        # 调用父类方法
        child_self.parent_result = parent_method(child_self, *args, **kwargs)
        # 调用子类方法并传入父类结果
        return func(child_self, *args, **kwargs)

    return wrapper


class Commands(HLLCommands):
    '''获取信息'''

    @call_parent_first
    def get_name(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_map(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_slots(self) -> tuple[int, int]:
        res = self.parent_result
        if res:
            num, slots = res.split("/")
            return int(num), int(slots)

    @call_parent_first
    def get_players(self) -> list[Any]:
        return self.parent_result

    @call_parent_first
    def get_playerIds(self) -> list[tuple[str, str]]:
        res = self.parent_result
        res = [(item.split(' : ')[1], item.split(' : ')[0]) for item in res]
        return res

    @call_parent_first
    def get_adminIds(self) -> list[tuple[str, str, str]]:
        res = self.parent_result
        res = [(item.split(' ', 2)[0], item.split(' ', 2)[1], item.split(' ', 2)[2].strip('"')) for item in res]
        return res

    @call_parent_first
    def get_vipIds(self) -> list[tuple[str, str]]:
        res = self.parent_result
        res = [(item.split(' ', 2)[0], item.split(' ', 2)[1].strip('"')) for item in res]
        return res

    @call_parent_first
    def get_adminGroups(self) -> list[str]:
        return self.parent_result

    @call_parent_first
    def get_tempBans(self) -> list[tuple[str, str, str, int, str, str]]:
        res = self.parent_result
        pattern = r'^(?:nickname "(.*?)" )?banned for (.*?) hours on ([\d\.\-]*)(?: for "(.*?)")?(?: by admin "(.*?)")?$'
        result = []
        for i in range(len(res)):
            if not res[i]:
                continue
            steam_id = res[i].split(' : ')[0]
            item = res[i].split(' : ')[1]
            matches = re.findall(pattern, item)
            if matches:
                nickname, hours, date, reason, admin = matches[0]
                time_array = time.strptime(date, "%Y.%m.%d-%H.%M.%S")
                time_stamp = int(time.mktime(time_array))
                result.append((steam_id, nickname, hours, time_stamp, reason, admin))
        return result

    @call_parent_first
    def get_permaBans(self) -> list[Any]:
        res = self.parent_result
        pattern = r'^(?:nickname "(.*?)" )?banned on ([\d\.\-]*)(?: for "(.*?)")?(?: by admin "(.*?)")?$'
        result = []
        for i in range(len(res)):
            if not res[i]:
                continue
            steam_id = res[i].split(' : ')[0]
            item = res[i].split(' : ')[1]
            matches = re.findall(pattern, item)
            if matches:
                nickname, date, reason, admin = matches[0]
                time_array = time.strptime(date, "%Y.%m.%d-%H.%M.%S")
                time_stamp = int(time.mktime(time_array))
                result.append((steam_id, nickname, time_stamp, reason, admin))
        return result

    @call_parent_first
    def get_teamSwitchCooldown(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_autobalanceEnabled(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_autoBalanceThreshold(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_kickIdleTime(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_highPing(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_maxQueuedPlayers(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_numVipSlots(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_profanity(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_voteKickEnabled(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_voteKickThreshold(self) -> str:
        return self.parent_result

    @call_parent_first
    def get_gameState(self) -> dict[str, Any]:
        res = self.parent_result
        pattern = r"Players: Allied: (\d+) - Axis: (\d+)\nScore: Allied: (\d+) - Axis: (\d+)\nRemaining Time: (.*?)\nMap: (.*?)\nNext Map: (.*?)"
        matches = re.findall(pattern, res)
        if matches:
            allied_players, axis_players, allied_score, axis_score, time, map_name, next_map = matches[0]
            return {
                'allied_players': allied_players,
                'axis_players': axis_players,
                'allied_score': allied_score,
                'axis_score': axis_score,
                'time': time,
                'map_name': map_name,
                'next_map': next_map
            }

    @call_parent_first
    def get_playerInfo(self, player_name) -> dict[str, Any]:
        res = self.parent_result
        pattern = r"Name: (.*?)\nsteamID64: (.*?)\nTeam: (.*?)\nRole: (?:(.*?)\nUnit: (.*?) - (.*?)\nLoadout: )?(.*?)\nKills: (\d+) - Deaths: (\d+)\nScore: C (\d+), O (\d+), D (\d+), S (\d+)\nLevel: (\d+)\n"
        matches = re.findall(pattern, res)
        if matches:
            name, steam_id, team, role, team_id, team_name, loadout, kills, deaths, c, o, d, s, level = matches[0]
            return {
                'name': name,
                'steam_id': steam_id,
                'team': team,
                'role': role,
                'team_id': team_id,
                'team_name': team_name,
                'loadout': loadout,
                'kills': kills,
                'deaths': deaths,
                'c': c,  # 战斗效率
                'o': o,  # 进攻效率
                'd': d,  # 防守效率
                's': s,  # 支援效率
            }

    @call_parent_first
    def get_rotList(self) -> list[Any]:
        res = self.parent_result
        pattern = r"(.*?)\n"
        matches = re.findall(pattern, res)
        return matches

    @call_parent_first
    def get_showLog(self, minutes, filter_word='') -> list[Any] | None: return self.parent_result
        # res = self.parent_result
        # if res == "EMPTY":
        #     return None
        # pattern = r"(.*?)\n"
        # matches = re.findall(pattern, res)
        #
        # if matches:
        #     return matches
        # return
        # 日志玩家击杀正则
        # pattern = r"\[(?:.*?) hours \((.*?)\)\] (.*?): (.*?)\((.*?)/(.*?)\) -> (.*?)\((.*?)/(.*?)\) with (.*?)\n"

    '''服务器设置'''

    @call_parent_first
    def do_set_kickIdleTime(self, minutes) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_highPing(self, milliseconds) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_autoBalanceEnabled(self, enabled) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_autoBalanceThreshold(self, num) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_TeamSwitchCooldown(self, minutes) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_maxQueuedPlayers(self, num) -> str:
        return self.parent_result

    def do_set_numVipSlots(self, num) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_voteKickEnabled(self, enabled) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_voteKickThreshold(self, threshold) -> str:
        return self.parent_result

    @call_parent_first
    def do_set_resetVoteKickThreshold(self) -> str:
        return self.parent_result

    '''RCON'''

    @call_parent_first
    def do_rcon(self, command: str) -> str:
        return self.parent_result

    '''发送消息'''

    @call_parent_first
    def do_announcement(self, welcome_msg) -> str:
        return self.parent_result

    @call_parent_first
    def do_unicast(self, player, msg='') -> str:
        return self.parent_result

    @call_parent_first
    def do_broadcast(self, msg) -> str:
        return self.parent_result

    '''惩戒'''

    @call_parent_first
    def do_punish(self, player_name, msg='') -> str:
        return self.parent_result

    @call_parent_first
    def do_kick(self, player_name, msg='') -> str:
        return self.parent_result

    '''封禁'''

    @call_parent_first
    def do_tempBan(self, player, duration_hours=2, reason='""', admin_name='') -> str:
        return self.parent_result

    @call_parent_first
    def do_permaBan(self, player, reason='""', admin_name='') -> str:
        return self.parent_result

    '''解封'''

    @call_parent_first
    def do_pardonTempBan(self, player) -> str:
        return self.parent_result

    @call_parent_first
    def do_pardonPermaBan(self, player) -> str:
        return self.parent_result

    '''敏感词,逗号分隔'''

    @call_parent_first
    def do_banProfanity(self, words) -> str:
        return self.parent_result

    @call_parent_first
    def do_unbanProfanity(self, words) -> str:
        return self.parent_result

    '''管理员'''

    @call_parent_first
    def do_adminAdd(self, player_id, group, comment='') -> str:
        return self.parent_result

    @call_parent_first
    def do_adminDel(self, player_id) -> str:
        return self.parent_result

    '''VIP'''

    @call_parent_first
    def do_vipAdd(self, player_id, description) -> str:
        return self.parent_result

    @call_parent_first
    def do_vipDel(self, player_id) -> str:
        return self.parent_result

    '''切换阵营'''

    @call_parent_first
    def do_switchTeamOnDeath(self, player_name) -> str:
        return self.parent_result

    @call_parent_first
    def do_switchTeamNow(self, player_name) -> str:
        return self.parent_result

    '''地图'''

    @call_parent_first
    def do_map(self, map_name, ordinal_number='') -> str:
        return self.parent_result

    @call_parent_first
    def do_rotAdd(self, map_name, after_map_name='', after_map_ordinal_number='') -> str:
        return self.parent_result

    @call_parent_first
    def do_rotDel(self, map_name, ordinal_num='') -> str:
        return self.parent_result

    @call_parent_first
    def do_rconPassword(self, old_passwd, new_passwd) -> str:
        return self.parent_result

