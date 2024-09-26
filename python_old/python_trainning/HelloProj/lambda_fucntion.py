# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:lambda_fucntion
# @Author: nebulabhm
# @Date:   2021/5/17 10:50
# @Description: 
# ---------------------------------------
def calculate_fun(opr):
	if opr == '+':
		return lambda a, b: (a + b)
	else:
		return lambda a, b: (a - b)

f1 = calculate_fun('+')
f2 = calculate_fun('-')

print(type(f1))

print("10 + 5 = {0}".format(calculate_fun(f1(10, 5))))
print("10 - 5 = {0}".format(calculate_fun(f2(10, 5))))

