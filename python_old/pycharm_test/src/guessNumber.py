#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:guessNumber.py
# @Author: nebulabhm
# @Date:   2018/12/24 11:14
# @Descreption: 
#---------------------------------------

import  sys

def compareNum(num):
    result = 3
    if num > desNum:
        print('Your guess is too high')
        result = 1
    elif num < desNum:
        print('Your guess is too low.')
        result = 2
    return result

desNum = 11
i = 0
print('I am thinking of a number between 1 and 20.')

while True:
    print('Take a guess.')
    comparVal = 0
    inputNum = int(input())
    comparVal = compareNum(inputNum)

    if comparVal == 3:
        print('Good job! You guessed my number in ' + str(i) + ' guesses!')
        sys.exit()

    i = i + 1