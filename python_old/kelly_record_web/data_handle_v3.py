# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-12 13:05:44
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-13 10:45:29
# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-09 11:29:34
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-09 16:38:02
# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-07 09:34:27
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-07 12:08:17

import pickle
from AthleteList import AthleteList

def get_coach_data(filename):
    try:
        with open(filename) as f:
            data = f.readline().strip().split(',')
            temp = AthleteList(data.pop(0), data.pop(0), data)
        return(temp)
    except IOError as ioerr:
            print('File error:' + str(ioerr))
            return(None)

def put_to_store(files_list):
    all_athletes = {}
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
    try:
        with open('athletes.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store): ' + str(ioerr))

    return(all_athletes)

def get_from_store():
    all_athletes = {}
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle.load(athf)
    except IOError as ioerr:
        print('File error (get_form_strore): ' + str(ioerr))

    return(all_athletes)

vera = AthleteList('Vera Vi')
vera.append('1.31')
print(vera.top3())
vera.extend(['2.22', "1-21", '2.22'])
print(vera.top3())
james = get_coach_data('james.txt')
julie = get_coach_data('julie.txt')
mikey = get_coach_data('mikey.txt')
sarah = get_coach_data('sarah.txt')

print(james.name + "'s fastest times are: " + str(james.top3()))
print(julie.name + "'s fastest times are: " + str(julie.top3()))
print(mikey.name + "'s fastest times are: " + str(mikey.top3()))
print(sarah.name + "'s fastest times are: " + str(sarah.top3()))
