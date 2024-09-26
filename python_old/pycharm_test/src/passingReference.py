#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:passingReference.py
# @Author: nebulabhm
# @Date:   2018/12/24 14:13
# @Descreption: 
#---------------------------------------

def eggs(someParameter):
    someParameter.append('hello')

spam = [1, 2, 3]
eggs(spam)
print(spam)