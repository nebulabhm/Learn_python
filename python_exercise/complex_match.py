'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-09-26 11:12:29
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-09-26 11:12:52
FilePath: \Learn_python\python_exercise\complex_match.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
age = 8

match age:
    case x if x < 10:
        print(f'x<10 years old:{x}')
    case 10:
        print('10 years old.')
    case 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18:
        print('11~18 years old.')
    case 19:
        print('19 years old')
    case _:
        print('not sure.')
        