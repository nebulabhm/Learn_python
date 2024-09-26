#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:characterCount.py
# @Author: nebulabhm
# @Date:   2018/12/24 14:54
# @Descreption: 
#---------------------------------------

import  pprint

message = 'It was a bright cold day in April, and the clocks were striking thirteen'

count = {}
for character in message:
    count.setdefault(character, 0)
    count[character] = count[character] + 1

pprint.pprint(count)
