# coding=utf-8
from lib.person import Person
from lib.pinyin import PinYin
from config import PINYIN


def generate_name(data, rule):
    result = set()
    pinyin = PinYin(PINYIN)
    pinyin.load_word()
    name_pinyin_list = map(pinyin.hanzi2pinyin, data)
    result.update(Person.generator_map(name_pinyin_list, rule))
    return result
