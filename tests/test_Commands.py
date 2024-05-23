#!/usr/bin/env python
# -*-coding:utf-8 -*-
from hell_rcon_core.Commands import Commands
from hell_rcon_core.base.HLLBaseTypes import ServerInfoType
# from hell_rcon_core.base.HLLCommands import logger

import logging
logging.basicConfig(format='%(levelname)s: %(message)s',
                    level=logging.DEBUG,
                    filename='test.log',
                    filemode='a')
logger = logging.getLogger('Command')
logger.setLevel(level=logging.DEBUG)

# formatter = logging.Formatter('%(levelname)s: %(message)s')
file_handler = logging.FileHandler('test2.log', encoding="utf-8")
# file_handler.setLevel(level=logging.INFO)
# file_handler.setFormatter(formatter)

logger.addHandler(file_handler)

if __name__ == '__main__':
    org = 'org'
    SERVER_INFO: ServerInfoType = {
        "host": "203.10.00.00",  # os.getenv("HLL_HOST"),
        "port": "29027",  # os.getenv("HLL_PORT"),
        "password": "XXXXX",  # os.getenv("HLL_PASSWORD"),
    } if org == 'FJ' else {
        "host": "202.165.00.00",
        "port": "29027",
        "password": "XXXXX",
    }
    ctl = Commands(SERVER_INFO)
    # logger.info(ctl.get_name())
    # logger.info(ctl.get_map())
    # logger.info(ctl.get_slots())
    # logger.info(ctl.get_players())
    # logger.info(ctl.get_playerIds())
    # logger.info(ctl.get_adminIds())
    # logger.info(ctl.get_vipIds())

    # logger.info(ctl.get_adminGroups())
    # logger.info(ctl.get_tempBans())
    # logger.info(ctl.get_permaBans())
    # logger.info(ctl.get_teamSwitchCooldown())
    # logger.info(ctl.get_autobalanceEnabled())
    # logger.info(ctl.get_autoBalanceThreshold())
    # logger.info(ctl.get_kickIdleTime())
    # logger.info(ctl.get_highPing())
    # logger.info(ctl.get_maxQueuedPlayers())
    # logger.info(ctl.get_numVipSlots())
    # logger.info(ctl.get_profanity())
    # logger.info(ctl.get_voteKickEnabled())
    # logger.info(ctl.get_voteKickThreshold())
    # logger.info(ctl.get_gameState())
    # logger.info(ctl.get_playerInfo(""))
    # logger.info(ctl.get_rotList())
    # msg = ctl.get_showLog(minutes=360, filter_word="")
    # for i in msg:
    #     logger.info(i)

