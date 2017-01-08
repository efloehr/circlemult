import sys
from PyQt5.QtWidgets import QApplication, QWidget


if __name__ == '__main__':
    # A single Application is required.
    app = QApplication(sys.argv)

    # A QWidget without a parent is a window.
    w = QWidget()
    w.resize(800, 600)
    w.move(200, 200)
    w.setWindowTitle('Multiplication Circle')
    
    # Show the window.
    w.show()
    
    # Enter the event loop, waiting for events.
    # When the application is closed, the program will exit.
    sys.exit(app.exec_())