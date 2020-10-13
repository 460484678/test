#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#教程笔记
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()
    覆盖了原本的QWidget的键盘事件处理方法，使得ESC键能执行窗口结束
#解释
这个例子中，我们替换了事件处理器函数keyPressEvent()。
"""
"""
ZetCode PyQt5 tutorial

In this example, we reimplement an
event handler.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Event handler')
        self.show()

    def keyPressEvent(self, e):
        if e.key() == Qt.Key_Escape:
            self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())