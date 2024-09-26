import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget

if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = QMainWindow()
    cw = QWidget()
    v_layout = QVBoxLayout()
    cw.setLayout(v_layout)

    window.setCentralWidget(cw)
    window.show()

    app.exec()
