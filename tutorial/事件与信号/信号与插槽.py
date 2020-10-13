#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
#教程笔记
该文件以一种极为简洁的方式实现了数值绑定滑动条
sld.valueChanged.connect(lcd.display)
当QSlider的数值发生变化，QLCDNumber的显示同步变化
#解释
这里是把滑块的变化和数字的变化绑定在一起。
sender是信号的发送者，receiver是信号的接收者，slot是对这个信号应该做出的反应。
"""
"""
ZetCode PyQt5 tutorial

In this example, we connect a signal
of a QSlider to a slot of a QLCDNumber.

Author: Jan Bodnar
Website: zetcode.com
Last edited: January 2017
"""

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QWidget, QLCDNumber, QSlider,
                             QVBoxLayout, QApplication)


class Example(QWidget):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        lcd = QLCDNumber(self)
        sld = QSlider(Qt.Horizontal, self)

        vbox = QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)

        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal and slot')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())