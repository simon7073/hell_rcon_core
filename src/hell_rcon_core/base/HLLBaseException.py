#!/usr/bin/env python
# -*-coding:utf-8 -*-


class HLLBaseException(Exception):
    pass

class HLLAuthError(HLLBaseException):
    pass

class HLLServerError(HLLBaseException):
    pass