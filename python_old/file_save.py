# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-08-31 16:31:39
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-01 14:23:59

import os
import sys
os.chdir('H:\my_workshop\program\python')

man = [ ]
other_man = [ ]

def print_lol(the_list, indent=False, level=0, fh=sys.stdout):
    for each_item in the_list:
        if isinstance(each_item, list):
            print_lol(each_item, indent, level+1, fh)
        else:
            if indent:
                for tab_stop in range(level):
                    print("\t", end='', file=fh)
                print(each_item, file=fh)
try:
    data = open('aaa.txt')
    for each_line in data:
        # if (not each_line.find('.') == -1):
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()   # strip()方法从字符串中去除不想要的空白符
            print(line_spoken)
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other_man.append(line_spoken)
            # print(role, end='')
            # print(' --- ', end='')
            # print(line_spoken, end='')
        except:
            pass
    data.close()
except:
    print('The datafile is missing!')

try:
    print(man)    # print to screen
    print(other_man)

    with open('man_data.txt', 'w') as man_file:
        print_lol(man, False, 0, man_file)
    with open('other_man_data.txt', 'w') as other_man_file:
        print_lol(other_man, False, 0, other_man_file)

    # a_file = open('a_data.txt', 'w')    # parameter 'w', print to file (clear mode)
    # c_file = open('c_data.txt', 'w')

    # print(a, file=a_file)
    # print(c, file=c_file)

except IOError as err:
    print('File error.' + str(err))

# 任何情况都会执行的代码
finally:
    man_file.close()
    other_man_file.close()


