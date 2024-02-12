from PyQt5.QtWidgets import QWidget
from .mc_card import Ui_mc_card
from qfluentwidgets import FluentIcon


class Mc_Card(QWidget, Ui_mc_card):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.TransparentToolButton.setIcon(FluentIcon.CHEVRON_RIGHT)

