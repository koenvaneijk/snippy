import sys
import tkinter as tk
from ctypes import *
from ctypes.wintypes import *
from io import BytesIO

from PIL import Image, ImageGrab
from PyQt5 import QtCore, QtGui, QtWidgets


class Snippy(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)
        self.setWindowTitle(' ')
        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(
            QtGui.QCursor(QtCore.Qt.CrossCursor)
        )
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.show()

    def paintEvent(self, event):
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('blue'), 1))
        qp.setBrush(QtGui.QColor(128, 128, 255, 128))
        qp.drawRect(QtCore.QRect(self.begin, self.end))

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        self.close()

        x1 = min(self.begin.x(), self.end.x())
        y1 = min(self.begin.y(), self.end.y())
        x2 = max(self.begin.x(), self.end.x())
        y2 = max(self.begin.y(), self.end.y())

        image = ImageGrab.grab(bbox=(x1, y1, x2, y2))

        HGLOBAL = HANDLE
        SIZE_T = c_size_t
        GHND = 0x0042
        GMEM_SHARE = 0x2000

        GlobalAlloc = windll.kernel32.GlobalAlloc
        GlobalAlloc.restype = HGLOBAL
        GlobalAlloc.argtypes = [UINT, SIZE_T]

        GlobalLock = windll.kernel32.GlobalLock
        GlobalLock.restype = LPVOID
        GlobalLock.argtypes = [HGLOBAL]

        GlobalUnlock = windll.kernel32.GlobalUnlock
        GlobalUnlock.restype = BOOL
        GlobalUnlock.argtypes = [HGLOBAL]

        CF_DIB = 8

        OpenClipboard = windll.user32.OpenClipboard
        OpenClipboard.restype = BOOL 
        OpenClipboard.argtypes = [HWND]

        EmptyClipboard = windll.user32.EmptyClipboard
        EmptyClipboard.restype = BOOL
        EmptyClipboard.argtypes = None

        SetClipboardData = windll.user32.SetClipboardData
        SetClipboardData.restype = HANDLE
        SetClipboardData.argtypes = [UINT, HANDLE]

        CloseClipboard = windll.user32.CloseClipboard
        CloseClipboard.restype = BOOL
        CloseClipboard.argtypes = None

        output = BytesIO()
        image.convert("RGB").save(output, "BMP")
        data = output.getvalue()[14:]
        output.close()

        hData = GlobalAlloc(GHND | GMEM_SHARE, len(data))
        pData = GlobalLock(hData)
        memmove(pData, data, len(data))
        GlobalUnlock(hData)

        OpenClipboard(None)
        EmptyClipboard()
        SetClipboardData(CF_DIB, pData)
        CloseClipboard()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = Snippy()
    window.show()
    app.aboutToQuit.connect(app.deleteLater)
    sys.exit(app.exec_())

    
