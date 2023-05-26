import sys
from PyQt5.QtWidgets import QWidget, QToolTip, QPushButton, QApplication, QMessageBox
from PyQt5.QtGui import QIcon, QFont


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('Calibri', 14))
        self.setToolTip('Это <b>подсказка</b> виджета')

        btn = QPushButton('Моя кнопка', self)
        btn.setToolTip('Это <b>подсказка</b> кнопки')
        btn.resize(btn.sizeHint())
        btn.move(100, 50)


        self.setGeometry(500, 500, 300, 220)
        self.setWindowTitle('Программа')
        self.setWindowIcon(QIcon('index.png'))
        self.show()

    def closeEvent(self, event):
        reply = QMessageBox.question(self, 'Quit', 'Are you sure you want to quit?', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
