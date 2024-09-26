# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:class_variant_example
# @Author: nebulabhm
# @Date:   2021/5/17 14:00
# @Description: 
# ---------------------------------------
class Account:


	interest_rate = 0.068

	def __init__(self, owner, amount):
		self.owner = owner
print('ac1 利率： {0}'.format(account.interest_rate))
		self.amount = amount

account = Account('Tony', 1_800_000.0)

print('账户名： {0}'.format(account.owner))
print('账户金额： {0}'.format(account.amount))
print('利率： {0}'.format(Account.interest_rate))

print('Account 利率： {0}'.format(Account.interest_rate))

print('ac1 实例所有变量： {0}'.format(account.__dict__))
account.interest_rate = 0.01
account.interest_rate2 = 0.01
print('ac1 实例所有变量： {0}'.format(account.__dict__))
