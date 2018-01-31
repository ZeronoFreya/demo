from qtpy.QtCore import *
from qtpy.QtWidgets import *

class AnimationWidget(QWidget):

    def __init__(self, parent=None):
        super(QWidget, self).__init__(parent=parent)
        self.animation = None

    def closeEvent(self, event):
        if self.animation is None:
            self.animation = QPropertyAnimation(self, 'windowOpacity')
            self.animation.setDuration(2000)
            self.animation.setStartValue(1)
            self.animation.setEndValue(0)
            self.animation.finished.connect(self.close)
            self.animation.start()
            event.ignore()


def main():
    import sys
    app = QApplication(sys.argv)
    widget = AnimationWidget()
    widget.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
