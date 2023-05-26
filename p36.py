
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow

class Window(QMainWindow):
    """Main Window."""
    def __init__(self, parent=None):
        """Initializer."""
        super().__init__(parent)
        self.setWindowTitle("Python Menus") # устанавливаете заголовок
        self.resize(600, 500) # размер окна
        self.centralWidget = QLabel("Текст программы") # отображения сообщений
        self.centralWidget.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # выравнивание
        self.setCentralWidget(self.centralWidget)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
