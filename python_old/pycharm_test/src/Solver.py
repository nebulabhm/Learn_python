# -*- coding: utf-8 -*-
# @FileName:Solver
# @Author: nebulabhm
# @Date:   2018/12/6 10:07
# @Descreption: ENTER CONTENT
import math


class Solver(object):
    def calculate(self):
        """

        @param a:
        @param b:
        @param c:
        @type a: int
        @type b: int
        @type c: int
        @return:
        """
        while True:
            a = int(input("a "))
            b = int(input("b "))
            c = int(input("c "))
            d = b ** 2 - 4 * a * c
            if d>=0:
                disc = math.sqrt(d)
                root1 = (-b + disc) / (2 * a)
                root2 = (-b - disc) / (2 * a)
                print(root1, root2)
                return root1, root2
            else:
                print('error!')


Solver().calculate()
