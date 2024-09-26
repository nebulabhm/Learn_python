# -*- coding: utf-8 -*-
# @FileName:ex8.py
# @Author: nebulabhm760
# @Date:   2016-09-20 14:40:04
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-20 14:43:27
# @Descreption: Printing, Printing

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % ("I had this thing.", "That you could type up right.", "But it didn't sing.", "So I said goodnight.")

