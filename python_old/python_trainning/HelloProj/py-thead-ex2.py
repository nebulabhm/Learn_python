# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:py-thead-ex2
# @Author: nebulabhm
# @Date:   2021/5/27 15:36
# @Description: 
# ---------------------------------------
import threading
import time


# 线程函数
def thread_body():
	# 当前线程名
	t = threading.current_thread()
	for n in range(5):
		# 当前线程名
		print(' 第 {0} 次执行线程 {1}'.format(n, t.name))
		# 线程休眠
		time.sleep(1)

		print(' 线程{0} 执行完成！'.format(t.name))

# 主函数
def main():
	# 创建线程对象 t1
	t1 = threading.Thread(target=thread_body)
	# 启动线程 t1
	t1.start()

	# 创建线程对象 t2
	t2 = threading.Thread(target=thread_body, name='MyThread')
	# 启动线程 t2
	t2.start()

if __name__ == '__main__':
	main()


