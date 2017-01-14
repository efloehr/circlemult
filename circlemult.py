import sys
import math
from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QPainter
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QSpinBox

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
        segments.append( (pointToCoords(start, modulus, radius),
                          pointToCoords(end, modulus, radius)) )

    return segments


# This class draws the circle and lines
class CircleWidget(QWidget):
    def __init__(self, parent=None):
        super(CircleWidget, self).__init__(parent)
        self.multiplier = 0
        self.modulus = 0
        
    def setMultiplier(self, multiplier):
        self.multiplier = multiplier
        self.update()
        
    def setModulus(self, modulus):
        self.modulus = modulus
        self.update()
        
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing, True)
        painter.translate(self.width() / 2, self.height() / 2)

        diameter = min(self.width(), self.height())
        radius = diameter / 2.0
        
        painter.drawEllipse(QRectF(-radius, -radius, diameter, diameter))

        segments = getLineSegments(self.multiplier, self.modulus, radius)
        for segment in segments:
            start = segment[0]
            end = segment[1]
            painter.drawLine(start[0], start[1], end[0], end[1])
            

# This class sets up the main window
class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()
        self.multiplier = 2
        self.modulus = 10
        self.initUI()
        
    def initUI(self):
        # Set up the layout
        layout = QHBoxLayout()
        self.setLayout(layout)
        
        # Add the circle widget
        self.circle = CircleWidget()
        self.circle.setMultiplier(self.multiplier)
        self.circle.setModulus(self.modulus)
        layout.addWidget(self.circle)
        
        # Add the buttons
        buttons = QWidget()
        buttons_layout = QVBoxLayout()
        buttons.setLayout(buttons_layout)
        
        buttons_layout.addWidget(QLabel('multiplier:'))
        self.mult_spinner = QSpinBox()
        self.mult_spinner.setMinimum(2)
        self.mult_spinner.setMaximum(2999)
        self.mult_spinner.setValue(self.multiplier)
        self.mult_spinner.valueChanged.connect(self.multiplierChanged)
        buttons_layout.addWidget(self.mult_spinner)
        
        buttons_layout.addWidget(QLabel('modulus:'))
        self.mod_spinner = QSpinBox()
        self.mod_spinner.setMinimum(2)
        self.mod_spinner.setMaximum(2999)
        self.mod_spinner.setValue(self.modulus)
        self.mod_spinner.valueChanged.connect(self.modulusChanged)
        buttons_layout.addWidget(self.mod_spinner)
        layout.addWidget(buttons)
        
        self.setGeometry(200, 200, 800, 600)
        self.setWindowTitle('Multiplication Circle')
        self.show()
        
    def multiplierChanged(self, multiplier):
        self.circle.setMultiplier(multiplier)
    
    def modulusChanged(self, modulus):
        self.circle.setModulus(modulus)
    
        
if __name__ == '__main__':
    # A single Application is required.
    app = QApplication(sys.argv)

    # Start the main window
    window = MainWindow()
    
    # Enter the event loop, waiting for events.
    # When the application is closed, the program will exit.
    sys.exit(app.exec_())