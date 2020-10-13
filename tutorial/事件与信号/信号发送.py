#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#教材笔记
该程序演示了如何自定义信号和信号产生到处理的过程
#解释
我们创建了一个叫closeApp的信号，这个信号会在鼠标按下的时候触发，事件与QMainWindow绑定。
class Communicate(QObject):
    closeApp = pyqtSignal()
Communicate类创建了一个pyqtSignal()属性的信号。
    self.c = Communicate()
    self.c.closeApp.connect(self.close)
closeApp信号QMainWindow的close()方法绑定。
    def mousePressEvent(self, event):
        self.c.closeApp.emit()
点击窗口的时候，发送closeApp信号，程序终止。
"""
"""
ZetCode PyQt5 tutorial

In this example, we show how to
emit a custom signal.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import pyqtSignal, QObject
from PyQt5.QtWidgets import QMainWindow, QApplication


class Communicate(QObject):
    closeApp = pyqtSignal()


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.c = Communicate()
        self.c.closeApp.connect(self.close)

        self.setGeometry(300, 300, 290, 150)
        self.setWindowTitle('Emit signal')
        self.show()

    def mousePressEvent(self, event):
        self.c.closeApp.emit()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())