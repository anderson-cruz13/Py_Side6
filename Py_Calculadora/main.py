import sys
from main_window import MainWindow  # type: ignore
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    # Criar a aplicação
    app = QApplication(sys.argv)
    window = MainWindow()

    # Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info(text="teste")
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # Loop de execução
    window.adjustFixedSize()
    window.show()
    app.exec()
