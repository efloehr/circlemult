import sys
from PyQt5.QtWidgets import QApplication, QWidget

# This class sets up the main window
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Multiplication Circle')
        self.show()
        
        
if __name__ == '__main__':
    # A single Application is required.
    app = QApplication(sys.argv)

    # Start the main window
    window = MainWindow()
    
    # Enter the event loop, waiting for events.
    # When the application is closed, the program will exit.
    sys.exit(app.exec_())