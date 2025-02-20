from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QLineEdit, QPushButton, QLabel, QListWidget, QHBoxLayout,
                            QFrame)  # Added QFrame here
from PyQt6.QtCore import Qt, QTimer, QPoint
from PyQt6.QtGui import QFont, QScreen, QCursor
import sys
import webbrowser
import os

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("程序控制")
        self.setFixedSize(400, 500)
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        
        # 只保留停靠属性
        self.docked = False
        self.dock_position = None
        self.auto_hide_enabled = True  # 添加自动隐藏状态标志
        self.hide_timer = QTimer(self)
        self.hide_timer.timeout.connect(self.auto_hide)
        self.hide_timer.setInterval(3000)  # 3秒无操作自动隐藏
        
        # 添加检测鼠标位置的定时器
        self.check_mouse_timer = QTimer(self)
        self.check_mouse_timer.timeout.connect(self.check_mouse_position)
        self.check_mouse_timer.setInterval(100)  # 每0.1秒检查一次
        self.check_mouse_timer.start()
        
        self.setStyleSheet("""
            QMainWindow {
                background-color: #f8f9fa;
            }
            QLabel {
                color: #202124;
            }
            QLineEdit {
                padding: 8px;
                border: 1px solid #dadce0;
                border-radius: 4px;
                background-color: white;
            }
            QLineEdit:focus {
                border: 2px solid #4285f4;
                outline: none;
            }
        """)
        
        # 创建主窗口部件和布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)
        
        # 创建标题栏
        title_bar = QHBoxLayout()
        title_label = QLabel("程序控制")
        title_label.setFont(QFont('Microsoft YaHei UI', 10))
        title_label.setStyleSheet("color: #202124; padding: 5px;")
        
        # 添加自动隐藏开关按钮
        self.auto_hide_button = QPushButton("自动隐藏：开")
        self.auto_hide_button.setFont(QFont('Microsoft YaHei UI', 10))
        self.auto_hide_button.clicked.connect(self.toggle_auto_hide)
        self.auto_hide_button.setFixedSize(100, 30)
        self.auto_hide_button.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                border: none;
                border-radius: 4px;
                font-size: 12px;
            }
            QPushButton:hover {
                background-color: #3b78e7;
            }
        """)
        
        # 创建最小化和关闭按钮
        min_button = QPushButton("─")
        min_button.clicked.connect(self.showMinimized)
        min_button.setFixedSize(30, 30)
        min_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #5f6368;
                border: none;
                font-size: 14px;
            }
            QPushButton:hover {
                background-color: #e8eaed;
            }
        """)
        
        close_button = QPushButton("×")
        close_button.clicked.connect(self.close)
        close_button.setFixedSize(30, 30)
        close_button.setStyleSheet("""
            QPushButton {
                background-color: transparent;
                color: #5f6368;
                border: none;
                font-size: 16px;
            }
            QPushButton:hover {
                background-color: #dc3545;
                color: white;
            }
        """)
        
        title_bar.addWidget(title_label)
        title_bar.addStretch()
        title_bar.addWidget(self.auto_hide_button)
        title_bar.addWidget(min_button)
        title_bar.addWidget(close_button)
        layout.addLayout(title_bar)
        
        # 创建分隔线
        separator = QFrame()
        separator.setFrameShape(QFrame.Shape.HLine)
        separator.setStyleSheet("background-color: #dadce0;")
        layout.addWidget(separator)
        
        # 创建输入提示标签
        prompt_label = QLabel("请在下方输入文字：")
        prompt_label.setFont(QFont('Microsoft YaHei UI', 12))
        layout.addWidget(prompt_label)
        
        # 创建输入框
        self.text_entry = QLineEdit()
        self.text_entry.setFont(QFont('Microsoft YaHei UI', 10))
        self.text_entry.returnPressed.connect(self.show_text)
        layout.addWidget(self.text_entry)
        
        # 创建按钮布局
        button_layout = QHBoxLayout()
        
        # 创建显示按钮
        self.show_button = QPushButton("显示输入的文字")
        self.show_button.setFont(QFont('Microsoft YaHei UI', 10))
        self.show_button.clicked.connect(self.show_text)
        self.show_button.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3b78e7;
            }
            QPushButton:pressed {
                background-color: #3367d6;
            }
        """)
        button_layout.addWidget(self.show_button)
        
        # 创建清空按钮
        self.clear_button = QPushButton("清空历史")
        self.clear_button.setFont(QFont('Microsoft YaHei UI', 10))
        self.clear_button.clicked.connect(self.clear_history)
        self.clear_button.setStyleSheet("""
            QPushButton {
                background-color: #4285f4;
                color: white;
                border: none;
                padding: 8px 16px;
                border-radius: 4px;
            }
            QPushButton:hover {
                background-color: #3b78e7;
            }
            QPushButton:pressed {
                background-color: #3367d6;
            }
        """)
        button_layout.addWidget(self.clear_button)
        layout.addLayout(button_layout)
        
        # 创建结果标签
        self.result_label = QLabel()
        self.result_label.setFont(QFont('Microsoft YaHei UI', 10))
        self.result_label.setWordWrap(True)
        layout.addWidget(self.result_label)
        
        # 创建历史记录标签
        history_label = QLabel("历史记录：")
        history_label.setFont(QFont('Microsoft YaHei UI', 12))
        layout.addWidget(history_label)
        
        # 创建历史记录列表
        self.history_list = QListWidget()
        self.history_list.setFont(QFont('Microsoft YaHei UI', 10))
        # 修改列表样式
        self.history_list.setStyleSheet("""
            QListWidget {
                background-color: white;
                border: 1px solid #dadce0;
                border-radius: 4px;
                padding: 4px;
            }
            QListWidget::item {
                padding: 4px;
                border-radius: 2px;
            }
            QListWidget::item:selected {
                background-color: #e8f0fe;
                color: #1a73e8;
            }
            QListWidget::item:hover {
                background-color: #f1f3f4;
            }
        """)
        layout.addWidget(self.history_list)

    def enterEvent(self, event):
        """鼠标进入窗口时显示"""
        if self.docked and not self.isVisible() and self.auto_hide_enabled:
            self.show()
        self.hide_timer.stop()

    def leaveEvent(self, event):
        """鼠标离开窗口时启动隐藏计时器"""
        if self.docked and self.auto_hide_enabled:
            self.hide_timer.start()

    def mousePressEvent(self, event):
        """记录鼠标按下位置用于拖动"""
        self.drag_position = event.globalPosition().toPoint() - self.frameGeometry().topLeft()
        event.accept()

    def mouseMoveEvent(self, event):
        """处理窗口拖动"""
        if event.buttons() == Qt.MouseButton.LeftButton:
            self.move(event.globalPosition().toPoint() - self.drag_position)
            self.check_dock_position()

    def check_dock_position(self):
        """检查是否需要停靠到屏幕边缘"""
        screen = QApplication.primaryScreen().geometry()
        pos = self.geometry()
        
        # 检查是否靠近屏幕边缘（20像素阈值）
        if pos.left() < 20:  # 左边缘
            self.move(0, pos.top())
            self.dock_position = 'left'
            self.docked = True
        elif pos.right() > screen.width() - 20:  # 右边缘
            self.move(screen.width() - pos.width(), pos.top())
            self.dock_position = 'right'
            self.docked = True
        else:
            self.docked = False
            self.dock_position = None

    def check_mouse_position(self):
        """检查鼠标位置，决定是否显示窗口"""
        if not self.isVisible() and self.docked:
            cursor_pos = QCursor.pos()
            screen = QApplication.primaryScreen().geometry()
            
            if self.dock_position == 'left' and cursor_pos.x() < 2:
                self.show()
            elif (self.dock_position == 'right' and 
                  cursor_pos.x() > screen.width() - 2):
                self.show()

    def auto_hide(self):
        """自动隐藏窗口"""
        if self.docked and self.auto_hide_enabled:
            self.hide()
            self.hide_timer.stop()

    def show_text(self):
        input_text = self.text_entry.text()
        if input_text:
            # 先添加到历史记录
            self.history_list.insertItem(0, input_text)
            
            # 处理特殊命令
            if input_text.lower() == "edge" or input_text.lower() == "打开edge":
                try:
                    edge_path = "C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"
                    if os.path.exists(edge_path):
                        webbrowser.register('edge', None, webbrowser.BackgroundBrowser(edge_path))
                        webbrowser.get('edge').open('https://www.bing.com')
                    else:
                        webbrowser.open('https://www.bing.com')
                    self.result_label.setText("已打开Edge浏览器")
                except Exception as e:
                    self.result_label.setText(f"无法打开浏览器：{str(e)}")
            elif input_text.lower() == "关闭edge":
                try:
                    os.system("taskkill /f /im msedge.exe")
                    self.result_label.setText("已关闭Edge浏览器")
                except Exception as e:
                    self.result_label.setText(f"无法关闭浏览器：{str(e)}")
            else:
                self.result_label.setText(f"你输入的文字是：{input_text}")
            self.text_entry.clear()
        else:
            self.result_label.setText("请输入文字！")
        
        if self.auto_hide_enabled:
            self.hide_timer.start()  # 操作后重新开始计时

    def clear_history(self):
        self.history_list.clear()
        self.result_label.clear()
        self.hide_timer.start()  # 操作后重新开始计时

    # 添加切换自动隐藏的方法
    def toggle_auto_hide(self):
        """切换自动隐藏功能"""
        self.auto_hide_enabled = not self.auto_hide_enabled
        
        if not self.auto_hide_enabled:
            # 关闭自动隐藏
            self.hide_timer.stop()
            self.check_mouse_timer.stop()
            self.show()
            self.auto_hide_button.setText("自动隐藏：关")
            self.auto_hide_button.setStyleSheet("""
                QPushButton {
                    background-color: #dc3545;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #c82333;
                }
            """)
        else:
            # 开启自动隐藏
            self.check_mouse_timer.start()
            if self.docked:
                self.hide_timer.start()
            self.auto_hide_button.setText("自动隐藏：开")
            self.auto_hide_button.setStyleSheet("""
                QPushButton {
                    background-color: #4285f4;
                    color: white;
                    border: none;
                    border-radius: 4px;
                    font-size: 12px;
                }
                QPushButton:hover {
                    background-color: #3b78e7;
                }
            """)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())