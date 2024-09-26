# --------------------------------------
# -*- coding: utf-8 -*-
# @FileName:wx-box-ex
# @Author: nebulabhm
# @Date:   2021/5/26 16:02
# @Description: 
# ---------------------------------------
import wx


# 自定义窗口类MyFrame
class MyFrame(wx.Frame):
	def __init__(self):
		super().__init__(parent=None, title=" Box布局 ", size=(300, 120))
		self.Center()		# 窗口居中
		# ToDO
		panel = wx.Panel(parent=self)
		# 创建垂直方向的Box布局管理器对象
		vbox = wx.BoxSizer(wx.VERTICAL)
		self.statictext = wx.StaticText(parent=panel, label='Button1 单击 ')
		# 添加静态文本到垂直Box布局管理器
		vbox.Add(self.statictext, proportion=2, flag=wx.FIXED_MINSIZE | wx.TOP | wx.CENTRE, border=10)

		b1 = wx.Button(parent=panel, id=10, label='Button1')
		b2 = wx.Button(parent=panel, id=11, label='Button2')
		self.Bind(wx.EVT_BUTTON, self.on_click, id=10, id2=20)
		# 创建水平方向的Box布局管理器对象
		hbox = wx.BoxSizer(wx.HORIZONTAL)
		# 添加 b1 到水平 Box 布局管理器
		hbox.Add(b1, 0, wx.EXPAND | wx.BOTTOM, 5)
		# 添加 b2 到水平 Box 布局管理器
		hbox.Add(b2, 0, wx.EXPAND | wx.BOTTOM, 5)

		# 将水平 Box 布局管理器到垂直 Box 布局管理器
		vbox.Add(hbox, proportion=1, flag=wx.CENTRE)

		panel.SetSizer(vbox)

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
