from PyQt5 import QtCore, QtGui, QtWidgets

from .uis.main_window import Ui_MainWindow

class MainWindow(Ui_MainWindow):
    def __init__(self, window):
        Ui_MainWindow.__init__(self)

        # main window setup
        self.window = window
        self.setupUi(window)

        # quit menu entry
        self.actionQuit.triggered.connect(self.quit)

    def quit(self):
        """Quite the application"""
        QtCore.QCoreApplication.instance().quit()
