import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QGridLayout,  # Grid tem mais recursos de layout
    QMainWindow,
    QWidget)

"""
-> QApplication (app)
    -> QMainWindow (window -> setCentralWidget)
        -> CentralWidget
            -> Layout
                -> Widget's
    -> show
-> exec
"""

app = QApplication(sys.argv)
window = QMainWindow()
central_widget = QWidget()
window.setCentralWidget(central_widget)
window.setWindowTitle("Janela principal")

botao = QPushButton("Texto do botão")
botao.setStyleSheet('font-size: 80px')
botao.show()  # Renderizar bottom

botao2 = QPushButton("Texto do botão 2")
botao2.setStyleSheet('font-size: 40px')
botao2.show()

layout = QGridLayout()  # Column
central_widget.setLayout(layout)
layout.addWidget(botao, 1, 1)  # Mesma row; column diferente
layout.addWidget(botao2, 1, 2)

# Bottom de renderização
status_bar = window.statusBar()
status_bar.showMessage("Mensagem na barra")

# Top de redenrização
menu_bar = window.menuBar()
menu_bar1 = menu_bar.addMenu("Mensagem de menu")
menu_bar_acao = menu_bar1.addAction("Primeira ação")


def slot_example(status_bar):
    status_bar.showMessage("Executado")


menu_bar_acao.triggered.connect(
    lambda: slot_example(status_bar))  # Ação de um menu


window.show()
app.exec()
