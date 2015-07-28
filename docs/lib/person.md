Class Person
=====

### attributes

+ `name`
    + desc: real name of target
    + type: list of string
+ `username`
    + desc: username of target
    + type: list of string
+ `email`
    + desc: email of target
    + type: list of string
+ `qq_number`
    + desc: QQ number of target
    + type: list of int
+ `mobile_phone`
    + desc: mobile phone number of target
    + type: list of int
+ `birthday`
    + desc: birthday of target
    + type: time.struct\_time
+ `company`
    + desc: company of target
    + type: str


### methods

+ `generator_map`
    + desc: generate passwords fragment by formatting function
    + params: `data`, type: str, desc: string which will be formatted
    + params: `formatter_list`, type: sequence of callable, desc: formatter functions
    + returns: list

+ `_generate_mail`
    + desc: generate passwords fragment from email
    + params: none
    + returns: list

+ `_generate_name`
    + desc: generate passwords fragment from username/real name/email id string
    + params: none
    + returns: list
    
+ `_generate_birthday`
    + desc: generate passwords fragment from birthday
    + params: none
    + returns: list
    
+ `_generate_company`
    + desc: generate passwords fragment from company
    + params: none
    + returns: list
    
+ `_generate_qq`
    + desc: generate passwords fragment from qq numbers
    + params: none
    + returns: list
  
+ `_generate_attached_info`
    + desc: generate passwords fragment from user attached information
    + params: none
    + returns: list
    
+ `generate_password`
    + desc: generate passwords
    + params: none
    + returns: list
    
+ `generate_password_with_dict`
    + desc: generate passwords with wake passwords dict
    + params: none
    + returns: list

