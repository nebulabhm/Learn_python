# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:print_tuple
# @Author: nebulabhm
# @Date:   2021/5/14 15:01
# @Description:
# ---------------------------------------

a = {21, 32, 43, 45}

for item in a:
	print(item)

print('----------')
for i, item in enumerate(a):
	print('{0} - {1}'.format(i, item))
