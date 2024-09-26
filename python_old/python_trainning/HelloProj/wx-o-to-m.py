# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:wx-o-to-m
# @Author: nebulabhm
# @Date:   2021/5/26 14:19
# @Description: 
# ---------------------------------------
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title=" 一对多事件处理 !", size=(300, 180))
		self.Center()		# 窗口居中
		# ToDO
		panel = wx.Panel(parent=self)
		self.statictext = wx.StaticText(parent=panel, pos=(110,15))
		b1 = wx.Button(parent=panel, id=10, label='Button1', pos=(100, 45))
		b2 = wx.Button(parent=panel, id=11, label='Button2', pos=(100, 85))
		self.Bind(wx.EVT_BUTTON, self.on_click, b1)
		self.Bind(wx.EVT_BUTTON, self.on_click, id=11)

	def on_click(self, event):
		event_id = event.GetId()
		print(event_id)			# <class 'wx._core.CommandEvent'>
		if event_id == 10:
			self.statictext.SetLabelText('Button1 单击 ')
		else:
			self.statictext.SetLabelText('Button2 单击 ')


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
