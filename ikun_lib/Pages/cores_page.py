
from PyQt5.QtCore import QEasingCurve
from PyQt5.QtWidgets import QWidget
from .cores import Ui_Cores
from ..Widgets.mc_card_card import Mc_Card
from qfluentwidgets import FluentIcon, FlowLayout, setFont, PopUpAniStackedWidget


class Cores(QWidget, Ui_Cores):
    def __init__(self, parent=None):
        super().__init__(parent=parent)
        self.setupUi(self)
        self.PushButton.setIcon(FluentIcon.DOWNLOAD)
        self.PushButton_2.setIcon(FluentIcon.SYNC)
        self.scrollAreaWidgetContents.setStyleSheet("background-color: rgb(48, 48, 48, 0);")
        self.SingleDirectionScrollArea.setStyleSheet("background-color: rgb(48, 48, 48, 0);")
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(48, 48, 48, 0);")
        self.SmoothScrollArea.setStyleSheet("background-color: rgb(48, 48, 48, 0);")

        self.layout = FlowLayout(needAni=True)
        self.gridLayout_5.addLayout(self.layout, 0, 0, 1, 1)

        # customize animation
        self.layout.setAnimation(250, QEasingCurve.OutQuad)

        self.layout.setContentsMargins(30, 30, 30, 30)
        self.layout.setVerticalSpacing(20)
        self.layout.setHorizontalSpacing(10)

        setFont(self.BreadcrumbBar, 26)
        self.BreadcrumbBar.addItem("core", '核心管理')

        self.BreadcrumbBar.currentIndexChanged.connect(lambda: self.stackedWidget_2.setCurrentIndex(0))


        for i in range(6):

            self.mc_card = Mc_Card()

            self.mc_card.setObjectName(f"mccard{i}")
            self.layout.addWidget(self.mc_card)
            self.mc_card.TransparentToolButton.clicked.connect(lambda *args, t=self.mc_card: self.addInterface(t.StrongBodyLabel.text()))


    def addInterface(self, mc_version):
        self.BreadcrumbBar.addItem(mc_version, mc_version)
        self.LineEdit.setText(mc_version)
        self.stackedWidget_2.setCurrentIndex(1)


