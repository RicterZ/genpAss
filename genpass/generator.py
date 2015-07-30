# coding=utf-8
from lib.person import Person
from lib.pinyin import PinYin
from config import PINYIN


def generate_name(data, rule):
    pinyin = PinYin(PINYIN)
    pinyin.load_word()
    name_pinyin_list = map(pinyin.hanzi2pinyin, data)
    return Person.generator_map(name_pinyin_list, rule)


def generate_id_string(data, rule):
    id_string = map(lambda x: x.split('@')[0], data)
    return set(Person.generator_map(id_string, rule))
