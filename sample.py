# coding: utf-8
from genpass import Password
from pprint import pprint

emails = [
    'ricter@chaitin.com',
    'panda@chaitin.com',
    'baka@chaitin.com',
    'nya@chaitin.com',
]
company = [u'长亭', 'chaitin']

result = {}
persons = [Password(information={'email': email, 'company': company}) for email in emails]

for person in persons:
    result[person.information['email']] = list(person.generate_password())

pprint(result)
