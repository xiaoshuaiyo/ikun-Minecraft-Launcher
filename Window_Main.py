import sys

from PyQt5.QtCore import Qt, QLocale
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QDesktopWidget  # 桌面类
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

        # 窗体大小
        screen = QDesktopWidget().screenGeometry()  # 自动适应屏幕宽高
        self.resize(screen.width() - screen.width()*0.6, screen.height() - screen.height()*0.5)  # 这里比电脑桌面宽高各缩小了一点，以免电脑的状态栏遮掉了自己的窗口状态栏
        screen = QDesktopWidget().screenGeometry()
        size = self.geometry()
        self.move((screen.width() - size.width()) / 2, (screen.height() - size.height()) / 2)


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