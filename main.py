
from PyQt6.QtWidgets import QApplication,QLabel,QWidget,QVBoxLayout
import platform

class App(QApplication):
    pass

def getStyle():
    if platform.platform().startswith("macOS"):
        return 'macos'

app = QApplication([])
app.setStyle(getStyle())
window = QWidget()
v_layout = QVBoxLayout()
label = QLabel('Hello World')
label.show()
app.exec()