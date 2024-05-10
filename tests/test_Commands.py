#!/usr/bin/env python
# -*-coding:utf-8 -*-
from hell_rcon_core.Commands import Commands
from hell_rcon_core.base.HLLBaseTypes import ServerInfoType
from hell_rcon_core.base.HLLCommands import logger

if __name__ == '__main__':
    org = 'JWH'
    SERVER_INFO: ServerInfoType = {
        "host": "203.10.98.41",  # os.getenv("HLL_HOST"),
        "port": "29027",  # os.getenv("HLL_PORT"),
        "password": "6g6jk",  # os.getenv("HLL_PASSWORD"),
    } if org == 'FJ' else {
        "host": "202.165.70.15",
        "port": "29027",
        "password": "46y84",
    }
    ctl = Commands(SERVER_INFO)
    # logger.info(ctl.get_name())
    # logger.info(ctl.get_map())
    # logger.info(ctl.get_slots())
    # logger.info(ctl.get_players())
    logger.info(ctl.get_playerIds())
    logger.info(ctl.get_adminIds())
    # logger.info(ctl.get_vipIds())
    # logger.info(ctl.get_adminGroups())
    logger.info(ctl.get_tempBans())
    logger.info(ctl.get_permaBans())
    # logger.info(ctl.get_teamSwitchCooldown())
    # logger.info(ctl.get_autobalanceEnabled())
    # logger.info(ctl.get_autoBalanceThreshold())
    logger.info(ctl.get_kickIdleTime())
    # logger.info(ctl.get_highPing())
    # logger.info(ctl.get_maxQueuedPlayers())
    # logger.info(ctl.get_numVipSlots())
    logger.info(ctl.get_profanity())
    # logger.info(ctl.get_voteKickEnabled())
    logger.info(ctl.get_voteKickThreshold())
    logger.info(ctl.get_gameState())
    logger.info(ctl.get_playerInfo("『𝓙𝓦𝓗』½青丘白泽"))
    logger.info(ctl.get_rotList())
    logger.info(ctl.get_showLog(1))
