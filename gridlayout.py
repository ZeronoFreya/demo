#!/usr/bin/env python3

from PyQt5.QtWidgets import *
import sys

class Window(QWidget):
    def __init__(self):
        QWidget.__init__(self)

        layout = QGridLayout()
        self.setLayout(layout)

        # label = QLabel("Label (0, 0)")
        # layout.addWidget(label, 0, 0)
        # label = QLabel("Label (0, 1)")
        # layout.addWidget(label, 0, 1)
        # label = QLabel("Label (1, 0) spanning 2 columns")
        # layout.addWidget(label, 1, 0, 1, 2)
        # label = QLabel("Label (1, 0) spanning 2 rows")
        # layout.addWidget(label, 0, 2, 2, 1)
        avatar = QVBoxLayout()
        avatar.addWidget(QLabel('avatar'))
        avatar.addWidget(QLabel('avatar'))

        ctrlLay = QHBoxLayout()
        ctrlLay.addWidget(QLabel('ctrlLay'))
        ctrlLay.addWidget(QLabel('ctrlLay'))

        toolLay = QHBoxLayout()
        toolLay.addWidget(QLabel('toolLay'))
        toolLay.addWidget(QLabel('toolLay'))

        layout.addLayout(avatar,0,0,2,1)
        layout.addLayout(ctrlLay,0,1)
        layout.addLayout(toolLay,1,1)

app = QApplication(sys.argv)

screen = Window()
screen.show()

sys.exit(app.exec_())
