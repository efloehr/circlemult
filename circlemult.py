import sys
import math
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout

radians = 2.0 * math.pi

def pointToCoords(point, modulus, radius):
    theta = radians * (point / modulus)
    x = radius * math.cos(theta)
    y = radius * math.sin(theta)
    return (x,y)
    
def getLineSegments(multiplier, modulus, radius):
    segments = []

    for start in range(modulus):
        end = (start * multiplier) % modulus
        segments.append( (pointToCoords(start, modulus, radius), pointToCoords(end, modulus, radius)) )

    return segments


# This class draws the circle and lines
class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)
        self.multiplier = 0
        self.modulus = 0
        
    def setMultiplier(self, multiplier):
        self.multiplier = multiplier
        
    def setModulus(self, modulus):
        self.modulus = modulus
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.translate(self.width() / 2, self.height() / 2)

        diameter = min(self.width(), self.height())
        radius = diameter / 2.0
        
        painter.drawEllipse(QRectF(-radius, -radius, diameter, diameter))

        segments = getLineSegments(10, 200, radius)
        for segment in segments:
            start = segment[0]
            end = segment[1]
            painter.drawLine(start[0], start[1], end[0], end[1])
            

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