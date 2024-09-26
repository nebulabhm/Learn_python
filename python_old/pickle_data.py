# -*- coding: utf-8 -*-
# @Author: nebulabhm760
# @Date:   2016-09-01 14:28:38
# @Last Modified by:   nebulabhm760
# @Last Modified time: 2016-09-01 14:38:10

import pickle

try:
    with open('mydata.pickle', 'wb') as mysavedata:
        pickle.dump([1, 2, 'three'], mysavedata)

    with open('mydata.pickle', 'rb') as myrestoredata:
        a_list = pickle.load(myrestoredata)
    with open('myrdata.txt', 'w' ) as restore_data:
        print(a_list, file=restore_data)

    print(a_list)
except IOError as err:
    print('File error: ' + str(err))
