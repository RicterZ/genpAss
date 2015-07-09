# genpAss
中国特色的弱口令生成器

### TODOs
+ [ ] --csv 参数指定用户列表批量生成密码

### What's new
-o 参数可以输出密码到指定文件

### Installation

    git clone https://github.com/RicterZ/genpAss
    cd genAss && python setup.py install

### Usage

    usage: genpass [-h] [-n [NAME [NAME ...]]] [-u [USERNAME [USERNAME ...]]]
                   [-q [QQ_NUMBER [QQ_NUMBER ...]]] [-e [EMAIL [EMAIL ...]]]
                   [-m [MOBILE_PHONE [MOBILE_PHONE ...]]] [-b BIRTHDAY] [--csv]
                   [--with-dict] [-o OUTPUT_FILE]

    User information

    optional arguments:
      -h, --help            show this help message and exit
      -n [NAME [NAME ...]], --name [NAME [NAME ...]]
                            real name of target
      -u [USERNAME [USERNAME ...]], --username [USERNAME [USERNAME ...]]
                            usernames of target, English only
      -q [QQ_NUMBER [QQ_NUMBER ...]], --qq [QQ_NUMBER [QQ_NUMBER ...]]
                            QQ numbers of target
      -e [EMAIL [EMAIL ...]], --email [EMAIL [EMAIL ...]]
                            email addresses of target
      -m [MOBILE_PHONE [MOBILE_PHONE ...]], --mobile [MOBILE_PHONE [MOBILE_PHONE ...]]
                            mobile phone/phone numbers of target
      -b BIRTHDAY, --birthday BIRTHDAY
                            birthday of target, format: %Y-%m-%d
      --csv                 csv files of users list
      --with-dict           generate password with weak password dictionary
      -o OUTPUT_FILE, --output OUTPUT_FILE
                            output result to a json file


生成姓名为`王大锤`，用户名为`dachui`和`dacc`，生日为`1995-12-21`，邮箱为`wangdachui@qq.com`的密码，并配合弱口令字典：

    $ genpass -n 王大锤 -u dachui,dacc -b 1995-12-21 -e wangdachui@qq.com --with-dict

可以修改弱口令字典`src/data/dict.txt`，以及增加密码规则`src/rules/rules.py`来增强密码数量。


### LICENSE
MIT
