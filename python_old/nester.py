# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-02 10:05:31
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-02 10:11:33

''' There is a function, named print_lol, The function can print a list '''
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item)
        else:
            print(each_item)
