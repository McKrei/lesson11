import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QAction, QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.newAct = QAction("New")
        self.openAct = QAction("Open...")
        self.saveAct = QAction("Save")
        self.fileMenu = self.menuBar().addMenu("Файл")
        self.fileMenu.addAction(self.newAct)
        self.fileMenu.addAction(self.openAct)
        self.fileMenu.addAction(self.saveAct)
        self.menuBar().addSeparator()

# # Область панели инструментов Положение в главном окне<br>
# # Qt.LeftToolBarArea    Левая сторона
# # Qt.RightToolBarArea   Правая сторона
# # Qt.TopToolBarArea     Верх



if __name__ == "__main__":

    app = QApplication(sys.argv)
    win = MainWindow()
    win.show()
    app.exec()
