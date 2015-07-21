Class PinYin
=======

### attributes
+ `word_dict`
    + desc: the pinyin-Chinese character dictionary
    + type: dict

+ `dict_file`
    + desc: dictionary file
    + type: string of file path

### methods
+ `load_word`
    + desc: load dictionary file to `word_dict`
    + params: none
    + returns: none

+ `hanzi2pinyin`
    + desc: transfer Chinese character to pinyin
    + params: string, type: str
    + returns: str
