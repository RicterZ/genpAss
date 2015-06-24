# genpAss
中国特色的弱口令生成器

### 安装

    git clone https://github.com/RicterZ/genpAss
    cd genAss && python setup.py install
    
### 用法


    Usage: genpass [options]

    Options:
      -h, --help            show this help message and exit
      -n NAME, --name=NAME  true name of target, split by ","
      -u USERNAME, --username=USERNAME
                            username of target, split by ","
      -b BIRTHDAY, --birthday=BIRTHDAY
                            birthday of target, format: %Y-%m-%d
      -q QQ_NUMBER, --qq=QQ_NUMBER
                            QQ number of target, split by ","
      -e EMAIL, --email=EMAIL
                            email of target, split by ","
      -f FILE, --file=FILE  json format file's path of target information
      --with-dict           generate password with weak password dictionary


生成姓名为`王大锤`，用户名为`dachui`和`dacc`，生日为`1995-12-21`，邮箱为`wangdachui@qq.com`的密码，并配合弱口令字典：

    $ genpass -n 王大锤 -u dachui,dacc -b 1995-12-21 -e wangdachui@qq.com --with-dict

可以修改弱口令字典`src/data/dict.txt`，以及增加密码规则`src/rules/rules.py`来增强密码数量。  
  
      
