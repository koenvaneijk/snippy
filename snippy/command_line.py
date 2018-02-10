from .snippy import Snippy

import sys
from PyQt5 import QtWidgets

def main():   
    app = QtWidgets.QApplication(sys.argv)
    window = Snippy()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())
