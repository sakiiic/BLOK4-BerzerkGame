from PyQt5.QtWidgets import (QWidget, QVBoxLayout, QPushButton, QFrame, QColorDialog, QMainWindow,
                             QSizePolicy, QLabel, QFontDialog, QApplication, QDesktopWidget)

from PyQt5.QtGui import QColor

import sys

appstyle="""
QMainWindow{
    background-color : black;
}
"""

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.frm = QFrame(self)

        self.setStyleSheet(appstyle)

        self.setGeometry(700, 700, 650, 580)
        self.setWindowTitle('Berzerk game')

        self.center()

        self.show()

    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
