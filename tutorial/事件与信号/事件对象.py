#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#教程笔记
本文介绍了事件处理器函数的参数事件对象e
传递了一些处理事件所需要的参数
例如鼠标事件传递了鼠标坐标x,y
注意当前例子只有当鼠标位于窗口范围内才能获取到鼠标位置
而且需要开启事件默认追踪
self.setMouseTracking(True)
#解释
e代表了事件对象。里面有我们触发事件（鼠标移动）的事件对象。
x()和y()方法得到鼠标的x和y坐标点，然后拼成字符串输出到QLabel组件里。
"""
"""
ZetCode PyQt5 tutorial

In this example, we display the x and y
coordinates of a mouse pointer in a label widget.

Author: Jan Bodnar
Website: zetcode.com
Last edited: August 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QApplication, QGridLayout, QLabel


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        grid.setSpacing(10)

        x = 0
        y = 0

        self.text = "x: {0},  y: {1}".format(x, y)

        self.label = QLabel(self.text, self)
        grid.addWidget(self.label, 0, 0, Qt.AlignTop)

        self.setMouseTracking(True)

        self.setLayout(grid)

        self.setGeometry(300, 300, 350, 200)
        self.setWindowTitle('Event object')
        self.show()

    def mouseMoveEvent(self, e):
        x = e.x()
        y = e.y()

        text = "x: {0},  y: {1}".format(x, y)
        self.label.setText(text)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())