from __future__ import unicode_literals
import sys
import os
import random
import matplotlib
# Make sure that we are using QT5
matplotlib.use('Qt5Agg')
# Uncomment this line before running, it breaks sphinx-gallery builds
from PyQt5 import QtCore, QtWidgets

from numpy import arange, sin, pi
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt5agg import NavigationToolbar2QT


from matplotlib.figure import Figure


class MplWidget(QtWidgets.QWidget):
    def __init__(self,*args,**kwargs):
        QtWidgets.QWidget.__init__(self,*args,**kwargs)
        self.setLayout(QtWidgets.QVBoxLayout())
        self.canvas = MplCanvas()
        self.toolbar = NavigationToolbar2QT(self.canvas, self)
        self.layout().addWidget(self.toolbar)
        self.layout().addWidget(self.canvas)
        return

class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100, fig=None):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.ax = fig.add_subplot(111)
        self.fig = fig

        self.compute_initial_figure()

        FigureCanvas.__init__(self, fig)
        self.setParent(parent)

        FigureCanvas.setSizePolicy(self,
                                   QtWidgets.QSizePolicy.Expanding,
                                   QtWidgets.QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def compute_initial_figure(self):
        pass



