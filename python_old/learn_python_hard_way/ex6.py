# -*- coding: utf-8 -*-
# @FileName:ex6.py
# @Author: nebulabhm760
# @Date:   2016-09-20 09:35:40
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-20 14:19:33
# @Descreption: String and Text

x = "There are %d tpes of people." %10
binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." %(binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "This is the left side of ..."
e = "a string with a right side."

print w + e
