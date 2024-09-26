# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:wx-hello-world
# @Author: nebulabhm
# @Date:   2021/5/25 9:38
# @Description: 
# ---------------------------------------
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title=" 第一个GUI程序 !", size=(400, 300), pos=(100,100))
		self.Center()		# 窗口居中
		# ToDO
		panel = wx.Panel(parent=self)
		statictext = wx.StaticText(parent=panel, label='Hello world!', pos=(10,10))


class App(wx.App):

	def OnInit(self):
		# 创建窗口对象
		frame = MyFrame()
		frame.Show()
		return True

	def OnExit(self):
		print(' 应用程序退出 ')
		return 0

if __name__ == '__main__':
	app = App()
	app.MainLoop()			# 进入主事件程序
