# coding=utf-8

VERSION = '0.2.1'
__author__ = 'ricter'
__email__ = 'ricterzheng@gmail.com'

import rules
import command
import config
import lib
from .lib.password import Password
from .lib.pinyin import PinYin


__all__ = ['rules', 'command', 'config', 'lib', 'VERSION', '__author__', '__email__', 'Password', 'PinYin']
