# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:py-thread-ex1
# @Author: nebulabhm
# @Date:   2021/5/27 15:25
# @Description: 
# ---------------------------------------
import threading

# 当前线程对象
t = threading.currentThread()
# 当前线程名
print(t.name)

# 返回当前处于活动状态的线程个数
print(threading.active_count())

# 当前线程对象
t = threading.main_thread()
# 主线程名
print(t.name)

