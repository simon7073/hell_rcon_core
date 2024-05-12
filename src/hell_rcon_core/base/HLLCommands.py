#!/usr/bin/env python
# -*-coding:utf-8 -*-
from typing import Any, Tuple, Dict, List

from .HLLBaseLogging import get_logger
from .HLLBaseTypes import ServerInfoType
from .HLLConnection import HLLConnection

logger = get_logger(__name__)


class HLLCommands:
    def __init__(self, config: ServerInfoType) -> None:
        self.config = config
        self.conn = HLLConnection()
        self.conn.connect(
            host=self.config["host"],
            port=self.config["port"],
            password=self.config["password"],
        )
        self.parent_result = None

    '''获取信息'''

    def get_name(self) -> str: return self.conn.get_request("get name")

    def get_map(self) -> str: return self.conn.get_request("get map")

    def get_slots(self) -> str | list[Any]: return self.conn.get_request("get slots")

    def get_players(self) -> list[Any]: return self.conn.get_request("get players", is_list=True)

    def get_playerIds(self) -> list[tuple[str, str]]:
        return self.conn.get_request("get PlayerIds", is_list=True)

    def get_adminIds(self) -> list[tuple[str, str, str]]:
        return self.conn.get_request("get AdminIds", is_list=True)

    def get_vipIds(self) -> list[tuple[str, str]]:
        return self.conn.get_request("get VipIds", is_list=True)

    def get_adminGroups(self) -> list[str]:
        return self.conn.get_request("get AdminGroups", is_list=True)

    def get_tempBans(self) -> list[tuple[str, str, str, int, str, str]]:
        return self.conn.get_request("get TempBans", is_list=True)

    def get_permaBans(self) -> list[Any]:
        return self.conn.get_request("get PermaBans", is_list=True)

    def get_teamSwitchCooldown(self) -> str: return self.conn.get_request("get TeamSwitchCooldown")

    def get_autobalanceEnabled(self) -> str: return self.conn.get_request("get AutobalanceEnabled")

    def get_autoBalanceThreshold(self) -> str: return self.conn.get_request("get AutoBalanceThreshold")

    def get_kickIdleTime(self) -> str: return self.conn.get_request("get KickIdleTime")

    def get_highPing(self) -> str: return self.conn.get_request("get HighPing")

    def get_maxQueuedPlayers(self) -> str: return self.conn.get_request("get MaxQueuedPlayers")

    def get_numVipSlots(self) -> str: return self.conn.get_request("get NumVipSlots")

    def get_profanity(self) -> str: return self.conn.get_request("get Profanity")

    def get_voteKickEnabled(self) -> str: return self.conn.get_request("get VoteKickEnabled")

    def get_voteKickThreshold(self) -> str: return self.conn.get_request("get VoteKickThreshold")

    def get_gameState(self) -> str: return self.conn.get_request("get GameState")

    def get_playerInfo(self, player_name) -> str: return self.conn.get_request(f"PlayerInfo {player_name}")

    def get_rotList(self) -> str: return self.conn.get_request("RotList")

    def get_showLog(self, minutes=1000, filter_word='') -> str:
        '''
            ShowLog <minutes-to-backtrack> ["filter"]
            minutes: 1020min = 17hours
            filter: keyword search
        '''
        return self.conn.get_request(f"ShowLog {minutes} {filter_word}")

    '''服务器设置'''

    def do_set_kickIdleTime(self, minutes) -> str: return self.conn.get_request(f"SetKickIdleTime {minutes}")

    def do_set_highPing(self, milliseconds) -> str: return self.conn.get_request(f"SetHighPing {milliseconds}")

    def do_set_autoBalanceEnabled(self, enabled) -> str: return self.conn.get_request(
        f"SetAutobalanceEnabled {enabled}")

    def do_set_autoBalanceThreshold(self, num) -> str: return self.conn.get_request(f"SetAutobalanceThreshold {num}")

    def do_set_TeamSwitchCooldown(self, minutes) -> str: return self.conn.get_request(
        f"SetTeamSwitchCooldown {minutes}")

    def do_set_maxQueuedPlayers(self, num) -> str: return self.conn.get_request(f"SetMaxQueuedPlayers {num}")

    def do_set_numVipSlots(self, num) -> str: return self.conn.get_request(f"SetNumVipSlots {num}")

    def do_set_voteKickEnabled(self, enabled) -> str: return self.conn.get_request(f"SetVoteKickEnabled {enabled}")

    def do_set_voteKickThreshold(self, threshold) -> str:
        '''threshold: PlayerCount,Threshold[,PlayerCount,Threshold,...]'''
        return self.conn.get_request(f"SetVoteKickThreshold {threshold}")

    def do_set_resetVoteKickThreshold(self) -> str: return self.conn.get_request(f"ResetVoteKickThreshold")

    '''RCON'''

    def do_rcon(self, command: str) -> str: return self.conn.get_request(command)

    '''发送消息'''

    def do_announcement(self, welcome_msg) -> str: return self.conn.get_request(f"say {welcome_msg}")

    def do_unicast(self, player, msg='') -> str: return self.conn.get_request(f"message {player} {msg}")

    def do_broadcast(self, msg) -> str: return self.conn.get_request(f"Broadcast {msg}")

    '''惩戒'''

    def do_punish(self, player_name, msg='') -> str: return self.conn.get_request(f"Punish {player_name} {msg}")

    def do_kick(self, player_name, msg='') -> str: return self.conn.get_request(f"Kick {player_name} {msg}")

    '''封禁'''

    def do_tempBan(self, player, duration_hours=2, reason='""', admin_name='') -> str:
        return self.conn.get_request(f"TempBan {player} {duration_hours} {reason} {admin_name}")

    def do_permaBan(self, player, reason='""', admin_name='') -> str:
        return self.conn.get_request(f"PermaBan {player} {reason} {admin_name}")

    '''解封'''

    def do_pardonTempBan(self, player) -> str: return self.conn.get_request(f"PardonTempBan {player}")

    def do_pardonPermaBan(self, player) -> str: return self.conn.get_request(f"PardonPermaBan {player}")

    '''敏感词,逗号分隔'''

    def do_banProfanity(self, words) -> str: return self.conn.get_request(f"BanProfanity {words}")

    def do_unbanProfanity(self, words) -> str: return self.conn.get_request(f"UnbanProfanity {words}")

    '''管理员'''

    def do_adminAdd(self, player_id, group, comment='') -> str: return self.conn.get_request(
        f"AdminAdd {player_id} {group} {comment}")

    def do_adminDel(self, player_id) -> str: return self.conn.get_request(f"AdminDel {player_id}")

    '''VIP'''

    def do_vipAdd(self, player_id, description) -> str: return self.conn.get_request(
        f"VipAdd {player_id} {description}")

    def do_vipDel(self, player_id) -> str: return self.conn.get_request(f"VipDel {player_id}")

    '''切换阵营'''

    def do_switchTeamOnDeath(self, player_name) -> str: return self.conn.get_request(f"SwitchTeamOnDeath {player_name}")

    def do_switchTeamNow(self, player_name) -> str: return self.conn.get_request(f"SwitchTeamNow {player_name}")

    '''地图'''

    def do_map(self, map_name, ordinal_number='') -> str: return self.conn.get_request(
        f"Map {map_name} {ordinal_number}")

    def do_rotAdd(self, map_name, after_map_name='', after_map_ordinal_number='') -> str:
        return self.conn.get_request(f"RotAdd {map_name} {after_map_name} {after_map_ordinal_number}")

    def do_rotDel(self, map_name, ordinal_num='') -> str: return self.conn.get_request(
        f"RotDel {map_name} {ordinal_num}")

    def do_rconPassword(self, old_passwd, new_passwd) -> str: return self.conn.get_request(
        f"RconPassword {old_passwd} {new_passwd}")
