'''
Author: nebulabhm nebulabhm@gmail.com
Date: 2024-09-26 16:31:00
LastEditors: nebulabhm nebulabhm@gmail.com
LastEditTime: 2024-09-26 16:31:39
FilePath: \Learn_python\python_exercise\iterator.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
# 首先获得Iterator对象:
it = iter([1, 2, 3, 4, 5])
# 循环:
while True:
    try:
        # 获得下一个值:
        x = next(it)
        print(x)
    except StopIteration:
        # 遇到StopIteration就退出循环
        break