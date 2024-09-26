#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:varfunc1.py
# @Author: nebulabhm
# @Date:   2018/12/24 10:50
# @Descreption: 
#---------------------------------------

def spam():
    eggs = 'spam local'
    print(eggs) #prints 'spam local'

def bacon():
    eggs = 'bacon local'
    print(eggs) # prints 'bacon local'
    spam()
    print(eggs) # prints 'bacon local'

eggs = 'global'
bacon()
print(eggs) # prints 'global'