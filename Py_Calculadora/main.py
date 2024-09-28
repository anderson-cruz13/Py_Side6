import sys
from main_window import MainWindow  # type: ignore
from variables import WINDOW_ICON_PATH
from display import Display
from info import Info
from style import setupTheme
from buttons import Button, ButtonsGrid
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon


if __name__ == "__main__":
    # Criar a aplicação
    app = QApplication(sys.argv)
    setupTheme(app)
    window = MainWindow()

    # Ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # Info
    info = Info(text="teste")
    window.addWidgetToVLayout(info)

    # Displat
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Botão
    buttonsGrid.addWidget(Button("9"), 0, 2)
    buttonsGrid.addWidget(Button("8"), 0, 1)
    buttonsGrid.addWidget(Button("7"), 0, 0)
    buttonsGrid.addWidget(Button("6"), 1, 2)
    buttonsGrid.addWidget(Button("5"), 1, 1)
    buttonsGrid.addWidget(Button("4"), 1, 0)
    buttonsGrid.addWidget(Button("3"), 2, 2)
    buttonsGrid.addWidget(Button("2"), 2, 1)
    buttonsGrid.addWidget(Button("1"), 2, 0)
    buttonsGrid.addWidget(Button("."), 3, 2)
    buttonsGrid.addWidget(Button("0"), 3, 1)
    buttonsGrid.addWidget(Button("+/-"), 3, 0)

    # Loop de execução
    window.adjustFixedSize()
    window.show()
    app.exec()
