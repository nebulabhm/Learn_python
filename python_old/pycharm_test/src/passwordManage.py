#--------------------------------------
# -*- coding: utf-8 -*-
# @FileName:passwordManage.py
# @Author: nebulabhm
# @Date:   2018/12/25 8:57
# @Descreption: An insecure password locker program
#---------------------------------------

PASSWORD = {'email': 'F7miniBDDuvMJuxESSKHFhTxFtjVB6',
            'blog': 'VmALvQyKAxiVH5G8v01if1MLZF3sdt',
            'luggage': '12345'}

import  sys, pyperclip
if len(sys.argv) < 2:
    print('Usage: python passwordManage.py [account] - copy account password')
    sys.exit()

account = sys.argv[1] # first command line arg is the account name

if account in PASSWORD:
    pyperclip.copy(PASSWORD[account])
    print('Password for ' + account + ' copied to clipboard.')
else:
    print('There is no account named ' + account)
