#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:zeroDivide.py
# @Author: nebulabhm
# @Date:   2018/12/24 10:59
# @Descreption: 
#---------------------------------------

def spam(divideBy):
    try:
        return 42 / divideBy
    except ZeroDivisionError:
        print('Error: Invalid argument.')


print(spam(42))
print(spam(12))
print(spam(0))
print(spam(1))