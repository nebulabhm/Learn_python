# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-02 10:43:43
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-07 09:45:57


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
with open('james.txt') as jaf:
    data = jaf.readline()
    james = data.strip().split(',') # method chaining
with open('julie.txt') as juf:
    data = juf.readline()
    julie = data.strip().split(',')
with open('mikey.txt') as mif:
    data = mif.readline()
    mikey = data.strip().split(',')
with open('sarah.txt') as saf:
    data = saf.readline()
    sarah = data.strip().split(',')
"""


def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline()
            return(data.strip().split(','))
    except IOError as ioerr:
        print('File error:' + str(ioerr))
        return(None)

james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

"""
clean_james = []
clean_julie = []
clean_mikey = []
clean_sarah = []

#  将清理后的数据追加到新列表中
for each_t in james:
    clean_james.append(sanitize(each_t))

for each_t in julie:
    clean_julie.append(sanitize(each_t))

for each_t in mikey:
    clean_mikey.append(sanitize(each_t))

for each_t in sarah:
    clean_sarah.append(sanitize(each_t))
"""
clean_james = sorted(set([sanitize(t) for t in james]))[0:3]
clean_julie = sorted(set([sanitize(t) for t in julie]))[0:3]
clean_mikey = sorted(set([sanitize(t) for t in mikey]))[0:3]
clean_sarah = sorted(set([sanitize(t) for t in sarah]))[0:3]

"""
print(james)
print(julie)
print(mikey)
print(sarah)
"""
"""
print(sorted(james))
print(sorted(julie))
print(sorted(mikey))
print(sorted(sarah))
"""
"""
print(sorted(clean_james))
print(sorted(clean_julie))
print(sorted(clean_sarah))
print(sorted(clean_mikey))
"""
print(clean_james)
print(clean_julie)
print(clean_mikey)
print(clean_sarah)
