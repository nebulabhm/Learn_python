# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:wx-window-ex
# @Author: nebulabhm
# @Date:   2021/5/24 16:05
# @Description: 
# ---------------------------------------
import wx


# 创建应用程序对象
app = wx.App()

# 创建窗口对象
frm = wx.Frame(None, title=" 第一个GUI程序！", size = (400, 300), pos = (100, 100))

frm.Show()		# 显示窗口

app.MainLoop()	# 进入主事件循环


