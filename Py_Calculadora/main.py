import sys
from main_window import MainWindow  # type: ignore
from PySide6.QtWidgets import QApplication, QLabel

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('Teste')
    label1.setStyleSheet('font-size: 50px')
    window.v_layout.addWidget(label1)

    window.show()
    app.exec()
