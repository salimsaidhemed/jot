
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout,QMainWindow
import platform
import sys

class MainWindow(QMainWindow):

    # def getStyle(self):
    #     if platform.platform().startswith("macOS"):
    #         return 'macos'
    
    def __init__(self):
        super(MainWindow,self).__init__()
        self.setGeometry(50,50,500,300)
        self.setWindowTitle("Jot")
        # self.setStyle(self.getStyle())
        self.show()


if __name__ == "__main__":
    
    app = QApplication([])
    app.setStyle('macos')
    MainWindow().show()
    sys.exit(app.exec())
    