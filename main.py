import sys
from PySide6.QtWidgets import (
    QApplication,
    QPushButton,
    QVBoxLayout,
    QWidget)

app = QApplication(sys.argv)

botao = QPushButton("Texto do botão")
botao.setStyleSheet('font-size: 80px')
botao.show()  # Renderizar bottom
botao2 = QPushButton("Texto do botão 2")
botao2.setStyleSheet('font-size: 40px')
botao2.show()

central_widget = QWidget()
layout = QVBoxLayout()  # Column
central_widget.setLayout(layout)
layout.addWidget(botao)
layout.addWidget(botao2)

central_widget.show()
app.exec()
