import platform
from datetime import datetime
from os import getpid
import qfluentwidgets
from psutil import Process


class report:
    def __init__(self):
        self.system_v = (
            f"{platform.system()} {'11' if int(platform.version().split('.')[-1]) >= 22000 else '10'} {platform.version()}"
            if platform.system() == "Windows" and platform.release() == "10"
            else f"{platform.system()} {platform.release()}"
        )
        self.qfw_v = qfluentwidgets.__version__
        self.python_v = platform.python_version()
        self.architecture_v = platform.architecture()[0]
        self.time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.ram = str(round(Process(getpid()).memory_full_info().uss / 1024 / 1024, 2))+"MB"

    def sys_info(self):

        sys_info = [self.system_v, self.qfw_v, self.python_v, self.architecture_v, self.time, self.ram]

        return sys_info

print(report().sys_info())