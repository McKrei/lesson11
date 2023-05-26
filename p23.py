import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(500, 500, 600, 220)
        self.move(800, 600)
        self.setWindowTitle('Текст окна')
        self.setWindowIcon(QIcon('22.png'))
        self.toolTip('<h1>New app</h1>')
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())