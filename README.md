# genpAss
中国特色的弱口令生成器


### Installation

    git clone https://github.com/RicterZ/genpAss
    cd genAss && python setup.py install

### Usage


    usage: genpass [-h] [-n [NAME [NAME ...]]] [-u [USERNAME [USERNAME ...]]]
                   [-q [QQ_NUMBER [QQ_NUMBER ...]]] [-e [EMAIL [EMAIL ...]]]
                   [-m [MOBILE_PHONE [MOBILE_PHONE ...]]] [-b BIRTHDAY]
                   [-c COMPANY] [--csv CSV] [--with-dict] [-o OUTPUT_FILE]

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
      -c COMPANY, --company COMPANY
                            company(english only)/website domain of target
      --csv CSV             csv files of users list
      --with-dict           generate passwords with weak password dictionary
      -o OUTPUT_FILE, --output OUTPUT_FILE
                            output result to a json file

假定一个人的信息如下：  


|字段|信息|
|-----|-----|
|姓名|王大锤|
|用户名|dachui,dac|
|QQ|818271273|
|手机|13928182828|
|邮箱|wangdac@gmail.com|
|生日|1993-12-21|
|公司|baidu|

可以根据以上信息生成密码：   

    genpass -n 王大锤 -u dachui dac -b 1993-12-21 -c baidu -m 13928182828 -q 818271273 -e wangdac@gmail.com

同时可以添加`--with-dict`来根据常见弱口令组合密码。   
另外可以通过`--csv`指定 csv 文件批量生成密码，csv 文件格式为：  

    name,email,birthday,username,mobile_phone,qq_number,company,
    测试,ceshi@x.com,1995-01-03,test cece,18883866666,23591712,google,
    大头,datou@x.com,1996-03-03,bighead,18883877777 18883899999,392912031,baidu,


### LICENSE
MIT
