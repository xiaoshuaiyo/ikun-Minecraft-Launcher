from PyQt5.QtWidgets import QWidget
from .home import Ui_home
from qfluentwidgets import FluentIcon


class Home(QWidget, Ui_home):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.PrimaryPushButton.setIcon(FluentIcon.BASKETBALL)
