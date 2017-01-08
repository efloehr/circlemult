import sys
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout


# This class draws the circle
class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.translate(self.width() / 2, self.height() / 2)

        diameter = min(self.width(), self.height())
        
        painter.drawEllipse(QRectF(-diameter / 2.0,
                                   -diameter / 2.0, diameter, diameter))


# This class sets up the main window
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        # Set up the layout
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Add the circle widget
        circle = CircleWidget()
        layout.addWidget(circle)
        
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