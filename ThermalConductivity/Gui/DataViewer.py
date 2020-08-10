from PyQt5 import QtWidgets, QtGui, QtCore, Qt
from ThermalConductivity.Gui.__designer.dataviewer_style import Ui_MainWindow
from ThermalConductivity.Gui.__designer.parameters_dialog import (
    Ui_Dialog_Parameters)
from ThermalConductivity import Analysis as A
from ThermalConductivity import Utilities as U
from ThermalConductivity import Comparison as Comp

import sys
import os


class Dialog_Parameters(QtWidgets.QDialog):
    def __init__(self):
        super(Dialog_Parameters, self).__init__()
        self.ui = Ui_Dialog_Parameters()
        self.ui.setupUi(self)

        self.ui.buttonBox.clicked.connect(self.return_values)
        return

    def return_values(self):
        # Physical parameters
        w = float(self.ui.lineEdit_width.text())
        t = float(self.ui.lineEdit_thickness.text())
        L = float(self.ui.lineEdit_length.text())
        sign = self.ui.comboBox_sign.currentText()
        gain = float(self.ui.lineEdit_gain.text())

        if sign == "Positive":
            sign = 1
        else:
            sign = -1

        # Function parameters
        force_kxy = self.ui.comboBox_forceKxy.currentText()
        symmetrize = self.ui.comboBox_symmetrize.currentText()

        if force_kxy == "Optional":
            force_kxy = False
        elif force_kxy == "True":
            force_kxy = True
        elif force_kxy == "False":
            force_kxy = False

        if symmetrize == "Optional":
            symmetrize = True
        elif symmetrize == "True":
            symmetrize = True
        elif symmetrize == "False":
            symmetrize = False

        kwargs = dict()
        kwargs["w"] = w
        kwargs["t"] = t
        kwargs["L"] = L
        kwargs["sign"] = sign
        kwargs["gain"] = gain
        kwargs["symmetrize"] = symmetrize
        kwargs["force_kxy"] = force_kxy

        self.kwargs = kwargs
        return


class mywindow(QtWidgets.QMainWindow):
    resized = QtCore.pyqtSignal()

    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.resized.connect(self.resize_tree)

        # Left dock
        self.initialize_tree()
        self.initialize_actionFilesystem_tree()
        self.initialize_pushButton_loadFile()
        self.initialize_pushButton_clearFile()

        # Menu
        self.initialize_actionOpen()
        self.initialize_actionExit()

        # Tab widget
        self.initialize_tab_analysis()
        self.initialize_tab_comparison()

        # Plot
        self.initialize_pushButton_plot()
        self.initialize_pushButton_clearPlot()

    def resizeEvent(self, event):
        self.resized.emit()
        return

    def resize_tree(self):
        tree = self.ui.treeView
        tree.setColumnWidth(0, tree.width())
        return

    def initialize_tab_comparison(self):
        tab = self.ui.tab_comparision
        button = self.ui.pushButtonComparisonAddFile
        button.clicked.connect(self.addToDatasetFromFile)
        button2 = self.ui.pushButtonComparisonAddAnalysis
        button2.clicked.connect(self.addToDatasetFromAnalysis)
        button3 = self.ui.pushButtonComparisonRemove
        button3.clicked.connect(self.removeFromDataset)

    def initialize_tab_analysis(self):
        tab = self.ui.tab_analysis
        self.analysis_methods = {key: value for key, value in A.__dict__.items()
                                 if callable(value)}
        box_methods = self.ui.comboBoxAnalysisMethod
        box_methods.addItems([i for i in self.analysis_methods])

        compute = self.ui.pushButton_AnalysisCompute
        compute.clicked.connect(self.analyze_data)
        return

    def get_kwargs(self):
        dialog = Dialog_Parameters()
        dialog.exec_()
        kwargs = dialog.kwargs
        return kwargs

    def analyze_data(self):
        if hasattr(self, "filename") is False:
            pass
        else:
            box = self.ui.comboBoxAnalysisMethod
            method = self.analysis_methods[box.currentText()]
            if method == A.Conductivity:
                parameters = self.get_kwargs()
                with U.capture_stdout() as get_value:
                    self.data = method(self.filename, **parameters)
                    captured = get_value()
                if captured != "":
                    captured = captured.strip()
                    self.ui.label_filename.setText(captured)
                else:
                    pass
            else:
                self.data = method(self.filename)
                delattr(self, "filename")
            self.populate_tab_analysis()
        return

    def addToDatasetFromFile(self):
        if hasattr(self, "filename") is False:
            return
        else:
            if hasattr(self, "dataset") is False:
                self.dataset = Comp.Data_Set()
            else:
                pass
        dataset = self.dataset
        filename = self.filename
        measurement = Comp.Measurement(filename)
        dataset.Add_measurements([measurement])
        self.dataset = dataset
        filename = os.path.split(filename)[1]
        self.ui.comboBox_comparisonMeasurements.addItem(filename)
        self.populate_tab_comparison()
        return

    def populate_tab_comparison(self):
        data = self.dataset
        self.ui.comboBoxComparisonXaxis.clear()
        self.ui.comboBoxComparisonYaxis.clear()

        self.ui.comboBoxComparisonXaxis.addItems(data.measures)
        self.ui.comboBoxComparisonYaxis.addItems(data.measures)

        menu = QtWidgets.QMenu()
        self.parameters_menu = menu
        for key in data.parameters:
            action = QtWidgets.QAction(key, self)
            action.setCheckable(True)
            action.changed.connect(self.toggle_parameter)
            menu.addAction(action)
        menu.addAction(self.ui.actionOpen)
        self.ui.toolButtonComparisoParameters.setMenu(menu)
        self.parameters = []
        self.parameters_menu = menu

        return

    def populate_tab_analysis(self):
        data = self.data
        self.ui.comboBoxAnalysisXaxis.clear()
        self.ui.comboBoxAnalysisYaxis.clear()
        lists = [key for key,
                 value in data.__dict__.items() if type(value) == list]
        if "parameters" in lists:
            lists.remove("parameters")
        else:
            pass
        for i in lists:
            self.ui.comboBoxAnalysisXaxis.addItems(getattr(data, i))
            self.ui.comboBoxAnalysisYaxis.addItems(getattr(data, i))
        menu = QtWidgets.QMenu()
        self.parameters_menu = menu
        for key in data.parameters:
            action = QtWidgets.QAction(key, self)
            action.setCheckable(True)
            action.changed.connect(self.toggle_parameter)
            menu.addAction(action)
        self.ui.toolButtonAnalysisParameters.setMenu(menu)
        self.parameters = []
        self.parameters_menu = menu
        return

    def plot(self):
        tab = self.ui.tabWidget
        current = tab.tabText(tab.currentIndex())
        if current == "Analysis":
            if hasattr(self, "data") is False:
                return
            else:
                data = self.data
                x_axis = self.ui.comboBoxAnalysisXaxis.currentText()
                y_axis = self.ui.comboBoxAnalysisYaxis.currentText()
        elif current == "Comparison":
            if hasattr(self, "dataset") is False:
                return
            else:
                data = self.dataset
                x_axis = self.ui.comboBoxComparisonXaxis.currentText()
                y_axis = self.ui.comboBoxComparisonYaxis.currentText()
        else:
            return

        parameters = self.parameters
        canvas = self.ui.plotWidget.canvas
        fig = self.ui.plotWidget.canvas.fig
        ax = self.ui.plotWidget.canvas.ax
        data.Plot(y_axis, "-o", x_axis=x_axis,
                  parameters=parameters, show=True, fig=fig, ax=ax)
        if type(data) == A.Conductivity:
            canvas.figure.text(0.05, 0.01, data["sample"],
                               fontsize=16, va="bottom", ha="left")
        else:
            pass
        self.ui.plotWidget.canvas.draw()
        return

    def toggle_parameter(self):
        menu = self.parameters_menu
        parameters = []
        actions = menu.actions()
        parameters += [i.text() for i in actions if i.isChecked() is True]
        self.parameters = parameters
        return

    def initialize_pushButton_clearFile(self):
        button = self.ui.pushButton_clearFile
        button.clicked.connect(self.clearFile)
        return

    def initialize_tree(self):
        tree = self.ui.treeView
        model = QtWidgets.QFileSystemModel()
        model.setRootPath("")
        tree.setModel(model)
        tree.scrollTo(model.index(QtCore.QDir.currentPath()))
        tree.setSortingEnabled(True)
        tree.setIndentation(5)
        return

    def initialize_pushButton_clearPlot(self):
        button = self.ui.pushButton_clearPlot
        button.clicked.connect(self.clearPlot)
        return

    def clearPlot(self):
        canvas = self.ui.plotWidget.canvas
        ax = canvas.ax
        canvas.figure.clear()
        canvas.figure.add_axes(ax)
        canvas.ax.clear()
        canvas.draw()
        for i in self.parameters_menu.actions():
            if i.isChecked() is True:
                i.setChecked(False)
            else:
                pass
        return

    def initialize_pushButton_loadFile(self):
        button = self.ui.pushButton_loadFile
        button.clicked.connect(self.file_no_dialog)
        return

    def initialize_actionFilesystem_tree(self):
        filesystem = self.ui.actionFilesystem_tree
        dock = self.ui.dockWidget_1
        state = filesystem.isChecked()
        filesystem.changed.connect(self.toggle_dock)

    def toggle_dock(self):
        dock = self.ui.dockWidget_1
        state_box = self.ui.actionFilesystem_tree.isChecked()
        state_dock = dock.isVisible()
        if state_dock is True and state_box is False:
            dock.setVisible(False)
        elif state_dock is False and state_box is True:
            dock.setVisible(True)
        else:
            pass
        return

    def initialize_pushButton_plot(self):
        button = self.ui.pushButton_plot
        button.clicked.connect(self.plot)
        return

    def initialize_actionExit(self):
        exit = self.ui.actionExit
        exit.triggered.connect(self.close)
        return

    def initialize_actionOpen(self):
        actionOpen = self.ui.actionOpen
        actionOpen.triggered.connect(self.file_dialog)
        return

    def file_dialog(self):
        cur_dir = QtCore.QDir.currentPath()
        filename = QtWidgets.QFileDialog.getOpenFileName(self, cur_dir)[0]
        if os.path.isfile(filename) is False:
            return
        else:
            self.filename = filename
            label = ("Loaded %s" % filename)
            self.ui.label_filename.setText(label)
        return

    def file_no_dialog(self):
        tree = self.ui.treeView
        model = tree.model()
        filename = os.path.abspath(model.filePath(tree.currentIndex()))
        if os.path.isfile(filename) is False:
            return
        else:
            self.filename = filename
            label = ("Loaded %s" % filename)
            self.ui.label_filename.setText(label)
        return

    def clearFile(self):
        if hasattr(self, "filename") is True:
            filename = self.filename
            delattr(self, "filename")
        else:
            pass
        label = ("No file loaded")
        self.ui.label_filename.setText(label)
        return

    def removeFromDataset(self):
        if hasattr(self, "dataset") is True:
            dataset = self.dataset
            measurements = dataset.measurements
            if len(measurements) == 0:
                return
            else:
                index = self.ui.comboBox_comparisonMeasurements.currentIndex()
                measurements.pop(index)
                self.ui.comboBox_comparisonMeasurements.removeItem(index)
                dataset = Comp.Data_Set(measurements)
                self.dataset = dataset
                self.populate_tab_comparison()
                if len(measurements) == 0:
                    delattr(self, "dataset")
                else:
                    pass
        else:
            pass
        return

    def addToDatasetFromAnalysis(self):
        if hasattr(self, "data") is False:
            return
        else:
            if hasattr(self.data, "Convert_to_Measurement") is False:
                return
            else:
                pass

        if hasattr(self, "dataset") is False:
            self.dataset = Comp.Data_Set()
        else:
            pass

        dataset = self.dataset
        filename = self.data["filename"]
        measurement = self.data.Convert_to_Measurement()
        dataset.Add_measurements([measurement])
        self.dataset = dataset
        filename = os.path.split(filename)[1]
        self.ui.comboBox_comparisonMeasurements.addItem(filename)
        self.populate_tab_comparison()
        return


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.show()
    sys.exit(app.exec())
