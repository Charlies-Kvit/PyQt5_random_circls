import sys
import random

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import Qt, QPoint
from UI import Ui_MainWindow


class DrawApp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.flag = False
        self.qp = QPainter()
        self.pushButton.clicked.connect(self.run)

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, events):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw()
            self.qp.end()

    def draw(self):
        rand = random.randrange
        self.qp.setBrush(QColor(rand(255), rand(255), rand(255)))  
        n = random.randint(5, 20)
        for i in range(n):
            r = random.randrange(100)
            coords = random.randrange(ex.frameGeometry().width() - 100), random.randrange(ex.frameGeometry().height() - 100)
            self.qp.drawEllipse(*coords, r, r)

    def run(self):
        self.drawf()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawApp()
    ex.show()
    sys.exit(app.exec())