# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:py-thread-ex4
# @Author: nebulabhm
# @Date:   2021/5/28 10:31
# @Description: 
# ---------------------------------------
import threading
import time


class TicketDB:
	def __init__(self):
		# 机票的数量
		self.ticket_count = 5

	# 获得当前机票数量
	def get_ticket_count(self):
		return self.ticket_count

	# 销售机票
	def sell_ticket(self):
		# TODO 等于用户付款
		# 线程休眠，阻塞当前线程，模拟等待用户付款
		time.sleep(1)
		print(" 第 {0} 号票，已经售出 ".format(self.ticket_count))
		self.ticket_count -= 1

# 创建TicketDB对象
db = TicketDB()

# 线程体1函数
def thread1_body():
	global db 	# 全局变量
	while True:
		curr_ticket_count = db.get_ticket_count()
		# 查询是否有机票
		if curr_ticket_count > 0:
			db.sell_ticket()
		else:
			# 无票退出
			break

# 线程体2函数
def thread2_body():
	global db 	# 全局变量
	while True:
		curr_ticket_count = db.get_ticket_count()
		# 查询是否有机票
		if curr_ticket_count > 0:
			db.sell_ticket()
		else:
			# 无票退出
			break


# 主函数
def main():
	# 创建线程对象 t1
	t1 = threading.Thread(target=thread1_body)
	# 启动线程 t1
	t1.start()
	# 创建线程对象 t2
	t2 = threading.Thread(target=thread2_body)
	# 启动线程 t2
	t2.start()

if __name__ == "__main_":
	main()

