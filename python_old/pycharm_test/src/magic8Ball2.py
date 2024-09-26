#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:magic8Ball2.py
# @Author: nebulabhm
# @Date:   2018/12/24 13:28
# @Descreption: 
#---------------------------------------

import  random

messages = ['It is certain',
            'It is decidedly so',
            'Yes definitely',
            'Reply hazy try agin',
            'Ask again later',
            'Concentrate and ask again',
            'My reply is no',
            'Outlook not so good',
            'Very doubtful']

print(messages[random.randint(0, len(messages) - 1)])
