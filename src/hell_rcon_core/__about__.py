#!/usr/bin/env python
# -*-coding:utf-8 -*-
import os.path

__all__ = [
    "__title__",
    "__summary__",
    "__uri__",
    "__version__",
    "__commit__",
    "__author__",
    "__email__",
    "__license__",
    "__copyright__",
]


try:
    base_dir = os.path.dirname(os.path.abspath(__file__))
except NameError:
    base_dir = None


__title__ = "hell_rcon_core"
__summary__ = "<Hell Let Loose> RCON API Core"
__description__ = "<Hell Let Loose> RCON API Core"
__url__ = "https://github.com/simon7073/hell_rcon_core"

__version__ = "0.1.2"

if base_dir is not None and os.path.exists(os.path.join(base_dir, ".commit")):
    with open(os.path.join(base_dir, ".commit")) as fp:
        __commit__ = fp.read().strip()
else:
    __commit__ = None

__author__ = "QingQiuBaiZe"
__author_email__ = "simoncq@163.com"

__license__ = "Apache License, Version 2.0"
__copyright__ = f"Copyright 2024 {__author__}"
