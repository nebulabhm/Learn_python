# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-01 10:34:44
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-01 10:44:36

try:
    data = open('missing.txt')
    print(data.readline(), end='')
except IOError as err:
    print('File error: ' +str(err)) #str() 函数强行转换为字符串
finally:
    if 'data' in locals():
        data.close()
