from PyQt4.QtGui import *
from PyQt4.QtCore import *
from PyQt4 import QtGui,QtCore
import sys

class Main(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.setFixedSize(600,500)

        self.tabBar=QTabBar(self)
        self.tabBar.setStyleSheet("QTabBar::tab{width:400px;}")
        self.tabBar.setExpanding(True)

        self.layout=QVBoxLayout(self)
        self.layout.addWidget(self.tabBar)

        self.tabBar.addTab("Kontext Menu")
        self.tabBar.addTab("Settings in detail")
        self.tabBar.addTab("Help and tips")
        self.tabBar.addTab("About")
        self.tabBar.addTab("Credits")

        self.show()

if __name__ == '__main__':
    app=QApplication(sys.argv)
    sd=Main()
    app.exec()
