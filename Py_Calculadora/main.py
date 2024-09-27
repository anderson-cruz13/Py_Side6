import sys
from main_window import MainWindow  # type: ignore
from PySide6.QtWidgets import QApplication, QLabel
from PySide6.QtGui import QIcon
from variables import WINDOW_ICON_PATH

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()

    label1 = QLabel('Teste')
    label1.setStyleSheet('font-size: 50px')
    window.addWidgetToVLayout(label1)
    window.adjustFixedSize()

    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    window.show()
    app.exec()
