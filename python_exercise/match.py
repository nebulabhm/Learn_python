'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-09-26 19:45:10
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-11-05 20:00:27
FilePath: \Learn_python\python_exercise\match.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
score = input('Please input your score:')

match score:
    case 'A':
        print('score is A.')
    case 'B':
        print('score is B.')
    case 'C':
        print('score is C.')
    case _: #default
        print('score is ???.')
    