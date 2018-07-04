#!/bin/python3
#-*- coding: utf-8 -*-

def p(x): print(x)
def pt(x): print(x, type(x))

import re, sip, time
from PyQt5.QtCore import *
from PyQt5.QtGui import *
import threading
import sys
from PyQt5.QtWidgets import (QApplication, QWidget, QPushButton,
QLineEdit, QInputDialog)

from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

class MyWebEngineView(QWebEngineView):
    def __init__(self, parent):
        super().__init__(parent)
        self.loop = 0
    def createWindow(self, webWindowType):
        self.loop += 1
        p('createWindow %02d' % (self.loop))
        return w.web

class MyWidget(QWidget):

    def __init__(self):
        super().__init__()
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.PluginsEnabled, True)
        QWebEngineSettings.globalSettings().setAttribute(QWebEngineSettings.FullScreenSupportEnabled, True)

        self.web = MyWebEngineView(self)
        self.web.resize(self.size())
        #self.web.load(QUrl("https://www.baidu.com/s?wd=1"))
        self.web.load(QUrl("https://www.bilibili.com/video/av24053091/"))
        # self.web.load(QUrl("http://www.youku.com"))
        # self.web.load(QUrl("http://music.163.com/#/playlist?id=2230693970"))
        # self.web.load(QUrl("https://www.w3.org/2010/05/video/mediaevents.html"))
        self.web.show()

        self.init()

    def resizeEvent(self, e):
        self.web.resize(self.size())

    def init(self):
        self.btn = QPushButton('按钮', self)
        self.btn.move(0, 0)
        self.btn.clicked.connect(self.btn_click)

        self.setGeometry(300, 300, 1000, 720)
        self.setWindowTitle('标题')
        self.show()

    def js_callback(self, result):
        p("js_callback: " + str(result))

    def btn_click(self):
        self.web.page().runJavaScript('''
        window.pyqt;
        ''', self.js_callback)

def timeout():
    w.web.page().runJavaScript('''
        window.pyqt = "pyqt";
''');

def urlChanged(x):
    p('urlChanged %s' % (x))

if __name__ == '__main__':
    sys.argv.append('--ppapi-flash-path=r:/pepflashplayer.dll')
    app = QApplication(sys.argv)

    w = MyWidget()
    w.web.urlChanged.connect(urlChanged)

    timer = threading.Timer(5, timeout)
    timer.start()
    sys.exit(app.exec_())
