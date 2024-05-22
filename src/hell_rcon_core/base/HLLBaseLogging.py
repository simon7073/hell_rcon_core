#!/usr/bin/env python
# -*-coding:utf-8 -*-
import logging

from rich.console import Console
from rich.logging import RichHandler

FORMAT = "%(message)s"
logging.basicConfig(
    level=logging.INFO, format=FORMAT, datefmt="[%X]", handlers=[RichHandler(console=Console(width=180))]
)


def get_logger(name):
    logger = logging.getLogger(name)
    return logger
