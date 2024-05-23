#!/usr/bin/env python
# -*-coding:utf-8 -*-
from hell_rcon_core.Commands import logger
from hell_rcon_core.base.HLLBaseTypes import ServerInfoType
from hell_rcon_core.base.HLLCommands import HLLCommands

if __name__ == "__main__":
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
    ctl = HLLCommands(SERVER_INFO)
    logger.info(ctl.get_name())
    logger.info(ctl.get_map())
    logger.info(ctl.get_slots())
    # logger.info(ctl.get_playerIds())
    logger.info(ctl.get_gameState())
    logger.info(ctl.get_showLog(1, 'KILL'))

    # logger.info(ctl.do_rconPassword("46y85", "46y84"))
