# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-07 09:34:27
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-07 12:08:17


def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter = ':'
    else:
        return(time_string)

    (mins, secs) = time_string.split(splitter)
    return(mins + '.' + secs)
"""
def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return(data.strip().split(','))
    except IOError as ioerr:
            print('File error:' + str(ioerr))
            return(None)
"""
def get_coach_data(filename):
    try:
        temp_data = {}
        with open(filename) as f:
            data = f.readline().strip().split(',')
            temp_data['Name'] = data.pop(0)
            temp_data['DOB'] = data.pop(0)
            temp_data['Times'] = sorted(set(sanitize(t) for t in data))[0:3]
            return(temp_data)
    except IOError as ioerr:
            print('File error:' + str(ioerr))
            return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

"""
# pop(0) 将删除并返回列表最前面的数据项
(james_name,james_dob) = james.pop(0), james.pop(0)
(julie_name,julie_dob) = julie.pop(0), julie.pop(0)
(mikey_name,mikey_dob) = mikey.pop(0), mikey.pop(0)
(sarah_name,sarah_dob) = sarah.pop(0), sarah.pop(0)
"""
"""
james_data = {}
james_data['Name'] = james.pop(0)
james_data['DOB'] = james.pop(0)
james_data['Times'] = james

julie_data = {}
julie_data['Name'] = julie.pop(0)
julie_data['DOB'] = julie.pop(0)
julie_data['Times'] = julie

mikey_data = {}
mikey_data['Name'] = mikey.pop(0)
mikey_data['DOB'] = mikey.pop(0)
mikey_data['Times'] = mikey

sarah_data = {}
sarah_data['Name'] = sarah.pop(0)
sarah_data['DOB'] = sarah.pop(0)
sarah_data['Times'] = sarah
"""
"""
# 引用dict中的数据
clean_james = sorted(set( [sanitize(t) for t in james_data['Times']]))[0:3]
clean_julie = sorted(set([sanitize(t) for t in julie_data['Times']]))[0:3]
clean_mikey = sorted(set([sanitize(t) for t in mikey_data['Times']]))[0:3]
clean_sarah = sorted(set([sanitize(t) for t in sarah_data['Times']]))[0:3]
"""
"""
clean_james = sorted(set( [sanitize(t) for t in james]))[0:3]
clean_julie = sorted(set([sanitize(t) for t in julie]))[0:3]
clean_mikey = sorted(set([sanitize(t) for t in mikey]))[0:3]
clean_sarah = sorted(set([sanitize(t) for t in sarah]))[0:3]
"""
"""
# list 和string 混合print时，需要使用str()函数将list转换为string
print(james_name + "'s fastest times are: " + str(clean_james))
print(julie_name + "'s fastest times are: " + str(clean_julie))
print(mikey_name + "'s fastest times are: " + str(clean_mikey))
print(sarah_name + "'s fastest times are: " + str(clean_sarah))
"""
print(james['Name'] + "'s fastest times are: " + str(james['Times']))
print(julie['Name'] + "'s fastest times are: " + str(julie['Times']))
print(mikey['Name'] + "'s fastest times are: " + str(mikey['Times']))
print(sarah['Name'] + "'s fastest times are: " + str(sarah['Times']))
