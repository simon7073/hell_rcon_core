#!/usr/bin/env python
# -*-coding:utf-8 -*-
import time

from hell_rcon_core.base.HLLConnection import HLLConnection

if __name__ == '__main__':
    # 202.165.70.15:29017 - 17u87
    # 203.10.98.41:29027 - 6g6jk

    # conn = HLLConnection("203.10.98.41", 29027, "6g6jk")
    # # conn.connect()
    # conn.send("ShowLog 60000")
    # conn.receive().decode()
    # # print(conn.receive().decode())
    # conn.close()
    with HLLConnection("203.10.98.41", "29027", "6g6jk") as conn:
        while True:
            try:
                conn.send("Get PlayerIds")
                print(conn.receive())
                time.sleep(1.5)
            except KeyboardInterrupt:
                break
"""
Get <Name|Map|Slots|Players|PlayerIds|AdminIds|VipIds|AdminGroups|TempBans|PermaBans|TeamSwitchCooldown|
AutobalanceEnabled|AutoBalanceThreshold|KickIdleTime|HighPing|MaxQueuedPlayers|NumVipSlots|
Profanity|VoteKickEnabled|VoteKickThreshold|GameState>
RconPassword <old-password> <new-password>
Say <welcome-message>
Map <new-map> [<ordinal-number>]
ShowLog <minutes-to-backtrack> ["filter"]
TempBan <"player-name"|"steam-64-id"> [<duration-hours>] ["reason"] ["admin-name"]
PardonTempBan <ban-details>
PermaBan <"player-name"|"steam-64-id"> ["reason"] ["admin-name"]
PardonPermaBan <ban-details>
Punish <"player-name"> ["reason"]
Kick <"player-name"> ["reason"]
SetKickIdleTime <minutes>
SetHighPing <milliseconds>
RotList
RotAdd <map-name> [<after-map-name>] [<after-map-ordinal-number>]
RotDel <map-name> [<ordinal-number>]
PlayerInfo <player-name>
SetAutobalanceEnabled <on|off>
SetAutobalanceThreshold <num-players>
SetTeamSwitchCooldown <minutes>
SetMaxQueuedPlayers <num-players>
SetNumVipSlots <num-slots>
SwitchTeamOnDeath <player-name>
SwitchTeamNow <player-name>
Broadcast <message>
AdminAdd <"steam-64-id"> <"admin-group"> ["comment"]
AdminDel <steam-64-id>
VipAdd <steam-64-id> <"description">
VipDel <steam-64-id>
BanProfanity <comma-separated-words>
UnbanProfanity <comma-separated-words>
SetVoteKickEnabled <on|off>
SetVoteKickThreshold <PlayerCount,Threshold[,PlayerCount,Threshold,...]>
ResetVoteKickThreshold
message <"player-name"|"steam-64-id"> ["message"]
"""
