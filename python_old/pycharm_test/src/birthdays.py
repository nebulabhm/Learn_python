#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:birthdays.py
# @Author: nebulabhm
# @Date:   2018/12/24 14:37
# @Descreption: 
#---------------------------------------

birthdays = {'Alice': 'Apr 1', 'Bob': 'Dec 12', 'Carol': 'Mar 4'}

while True:
    print('Enter a name: (blank to quit)')
    name = input()
    if name == 'quit':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')