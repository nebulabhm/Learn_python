'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-09-26 10:57:57
FilePath: \Learn_python\python_exercise\input.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
s = input('birth: ')
birth = int(s)
if birth < 2000:
    print('00前')
else:
    print('00后')