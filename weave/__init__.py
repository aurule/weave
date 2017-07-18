"""
Package for planning stories
"""

import argparse
import sys
from PyQt5 import QtCore, QtGui, QtWidgets

from . import gui
from .gui.main_window import MainWindow
from .__version__ import __version__

def start(argv=None):
    """
    Run the gui interface

    Args:
        argv (list): Arguments from the command invocation
    """

    parser = _make_parser()
    if not argv:
        argv = sys.argv[1:]
    args = parser.parse_args(argv)

    app = QtWidgets.QApplication(argv)
    window = QtWidgets.QMainWindow()

    prog = MainWindow(window)

    window.show()
    sys.exit(app.exec_())

def _make_parser():
    """
    Construct the arguments parser

    Returns:
        Complete argparser object
    """

    parser = argparse.ArgumentParser(description='Graphical story planning tool')

    return parser
