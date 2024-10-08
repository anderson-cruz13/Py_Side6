from typing import TYPE_CHECKING


from PySide6.QtWidgets import QPushButton, QGridLayout
from PySide6.QtCore import Slot
from variables import MEDIUM_FONT_SIZE
from utils import isNumOrDot, isValidNumber


if TYPE_CHECKING:
    from display import Display
    from info import Info
    from main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self) -> None:
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
            self,
            display: 'Display',
            info: 'Info',
            window: 'MainWindow',
            *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '<', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N', '0', '.', '=']
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = " "
        self._equationInitialValue = " "
        self._left = None
        self._right = None
        self._op = None

        self.equation = self._equationInitialValue
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self) -> None:
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backSpace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOp)

        for i, row in enumerate(self._gridMask):
            for j, buttonText in enumerate(row):
                button = Button(buttonText)

                if buttonText == '':
                    continue

                if not isNumOrDot(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)

                self.addWidget(button, i, j)
                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot) -> None:
        button.clicked.connect(slot)

    def _configSpecialButton(self, button) -> None:
        text = button.text()

        if text == 'C':
            # slot = self._makeSlot(self.display.clear)
            self._connectButtonClicked(button, self._clear)

        if text in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOp, text)
            )

        if text == '=':
            self._connectButtonClicked(button, self._eq)

        if text == 'N':
            self._connectButtonClicked(button, self._invertNumber)

        if text == '<':
            self._connectButtonClicked(button, self.display.backspace)

    def _makeSlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _invertNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newNumber = -float(displayText)

        if newNumber.is_integer():
            newNumber = int(newNumber)

        self.display.setText(str(newNumber))

    @Slot()
    def _insertToDisplay(self, text) -> None:
        newDisplayText = self.display.text() + text

        if not isValidNumber(newDisplayText):
            return

        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self) -> None:
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _configLeftOp(self, text) -> None:
        displayText = self.display.text()
        self.display.clear()
        self.display.setFocus()

        if not isValidNumber(displayText) and self._left is None:
            self._showError('Você não digitou nada.')

        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            self._showError('Conta incompleta.')
            return

        self._right = float(displayText)
        self._availableEquation()

    def _availableEquation(self) -> None:
        if self._left is not None and self._right is not None:
            try:
                if self._op == '+':
                    result = self._left + self._right
                elif self._op == '-':
                    result = self._left - self._right
                elif self._op == '*':
                    result = self._left * self._right
                elif self._op == '/':
                    if self._right == 0:
                        self._showError('Divisão por zero.')
                    result = self._left / self._right
                elif self._op == '^':
                    result = self._left ** self._right
                else:
                    result = "ERROR"
                    self.display.clear()
                    self.info.setText(result)
                    return

                # Limpa o display e exibe o resultado
                self.display.clear()
                self.info.setText(str(result))
                self._left = float(result)
                self._right = None

            except OverflowError:
                self.display.clear()
                self._showError('Essa conta não pode ser realizada.')
            except ZeroDivisionError as e:
                self.display.clear()
                self.info.setText(str(e))

        else:
            # Caso a operação ou o número da direita não esteja disponível
            if self._right is None and self._op is None:
                self.info.setText("")
                self.display.clear()
        self.display.setFocus()

    @Slot()
    def _backSpace(self):
        self.display.backspace()
        self.display.setFocus()

    def _makeDialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        self.display.setFocus()
        return msgBox

    def _showError(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _showInfo(self, text):
        msgBox = self._makeDialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
