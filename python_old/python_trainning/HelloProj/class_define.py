# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:class_define.example
# @Author: nebulabhm
# @Date:   2021/5/17 13:45
# @Description: 
# ---------------------------------------
class Animal(object):

	def __init__(self, age, sex, weight):
		self.age = age
		self.sex = sex
		self.weight = weight

animal = Animal(2, 1, 10.0)

print(' 年龄：{0}'.format(animal.age))
print(' 性别：{0}'.format(' 雌性 ' if animal.sex == 0 else ' 雄性 '))
print(' 体重：{0}'.format(animal.weight))
