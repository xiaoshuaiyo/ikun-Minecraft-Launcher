import sys

from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtWidgets import QApplication
from qfluentwidgets import FluentWindow, FluentIcon, FluentTranslator


from ikun_lib.Pages.home_page import Home
from ikun_lib.Pages.cores_page import Cores


class Window(FluentWindow):
    def __init__(self):
        super().__init__()

        # add Pages
        self.home = Home(self)
        self.addSubInterface(self.home,FluentIcon.HOME, "主页")
        self.cores = Cores(self)
        self.addSubInterface(self.cores, FluentIcon.GAME, "核心管理")


if __name__ == '__main__':
    # enable dpi scale
    QApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)


    app = QApplication(sys.argv)


    # i18n
    translator = FluentTranslator(QLocale(QLocale.Chinese))
    app.installTranslator(translator)


    w = Window()

    w.show()
    app.exec_()