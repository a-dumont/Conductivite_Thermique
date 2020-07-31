# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dataviewer_style.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1260, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.plotWidget = MplWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.plotWidget.sizePolicy().hasHeightForWidth())
        self.plotWidget.setSizePolicy(sizePolicy)
        self.plotWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.plotWidget.setObjectName("plotWidget")
        self.verticalLayout_2.addWidget(self.plotWidget)
        self.label_filename = QtWidgets.QLabel(self.centralwidget)
        self.label_filename.setText("")
        self.label_filename.setObjectName("label_filename")
        self.verticalLayout_2.addWidget(self.label_filename)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.widget.setObjectName("widget")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.tabWidget = QtWidgets.QTabWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tabWidget.setMinimumSize(QtCore.QSize(0, 0))
        self.tabWidget.setMaximumSize(QtCore.QSize(16777215, 150))
        self.tabWidget.setObjectName("tabWidget")
        self.tab_analysis = QtWidgets.QWidget()
        self.tab_analysis.setObjectName("tab_analysis")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_analysis)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.tab_analysis)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.comboBoxAnalysisYaxis = QtWidgets.QComboBox(self.tab_analysis)
        self.comboBoxAnalysisYaxis.setObjectName("comboBoxAnalysisYaxis")
        self.gridLayout.addWidget(self.comboBoxAnalysisYaxis, 1, 2, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.tab_analysis)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 0, 1, 1, 1)
        self.comboBoxAnalysisMethod = QtWidgets.QComboBox(self.tab_analysis)
        self.comboBoxAnalysisMethod.setObjectName("comboBoxAnalysisMethod")
        self.gridLayout.addWidget(self.comboBoxAnalysisMethod, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab_analysis)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 0, 2, 1, 1)
        self.comboBoxAnalysisXaxis = QtWidgets.QComboBox(self.tab_analysis)
        self.comboBoxAnalysisXaxis.setObjectName("comboBoxAnalysisXaxis")
        self.gridLayout.addWidget(self.comboBoxAnalysisXaxis, 1, 1, 1, 1)
        self.label_4 = QtWidgets.QLabel(self.tab_analysis)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 3, 1, 1)
        self.pushButton_AnalysisCompute = QtWidgets.QPushButton(self.tab_analysis)
        self.pushButton_AnalysisCompute.setObjectName("pushButton_AnalysisCompute")
        self.gridLayout.addWidget(self.pushButton_AnalysisCompute, 2, 0, 1, 1)
        self.toolButtonAnalysisParameters = QtWidgets.QToolButton(self.tab_analysis)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonAnalysisParameters.sizePolicy().hasHeightForWidth())
        self.toolButtonAnalysisParameters.setSizePolicy(sizePolicy)
        self.toolButtonAnalysisParameters.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButtonAnalysisParameters.setToolButtonStyle(QtCore.Qt.ToolButtonTextOnly)
        self.toolButtonAnalysisParameters.setAutoRaise(False)
        self.toolButtonAnalysisParameters.setArrowType(QtCore.Qt.DownArrow)
        self.toolButtonAnalysisParameters.setObjectName("toolButtonAnalysisParameters")
        self.gridLayout.addWidget(self.toolButtonAnalysisParameters, 1, 3, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 4, 0, 1, 1)
        self.tabWidget.addTab(self.tab_analysis, "")
        self.tab_comparision = QtWidgets.QWidget()
        self.tab_comparision.setObjectName("tab_comparision")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_comparision)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_7 = QtWidgets.QLabel(self.tab_comparision)
        self.label_7.setObjectName("label_7")
        self.gridLayout_3.addWidget(self.label_7, 0, 3, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.tab_comparision)
        self.label_6.setObjectName("label_6")
        self.gridLayout_3.addWidget(self.label_6, 0, 2, 1, 1)
        self.toolButtonComparisoParameters = QtWidgets.QToolButton(self.tab_comparision)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.toolButtonComparisoParameters.sizePolicy().hasHeightForWidth())
        self.toolButtonComparisoParameters.setSizePolicy(sizePolicy)
        self.toolButtonComparisoParameters.setPopupMode(QtWidgets.QToolButton.InstantPopup)
        self.toolButtonComparisoParameters.setObjectName("toolButtonComparisoParameters")
        self.gridLayout_3.addWidget(self.toolButtonComparisoParameters, 1, 3, 1, 1)
        self.comboBoxComparisonXaxis = QtWidgets.QComboBox(self.tab_comparision)
        self.comboBoxComparisonXaxis.setObjectName("comboBoxComparisonXaxis")
        self.gridLayout_3.addWidget(self.comboBoxComparisonXaxis, 1, 1, 1, 1)
        self.comboBoxComparisonYaxis = QtWidgets.QComboBox(self.tab_comparision)
        self.comboBoxComparisonYaxis.setObjectName("comboBoxComparisonYaxis")
        self.gridLayout_3.addWidget(self.comboBoxComparisonYaxis, 1, 2, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.tab_comparision)
        self.label_5.setObjectName("label_5")
        self.gridLayout_3.addWidget(self.label_5, 0, 1, 1, 1)
        self.label_11 = QtWidgets.QLabel(self.tab_comparision)
        self.label_11.setObjectName("label_11")
        self.gridLayout_3.addWidget(self.label_11, 0, 0, 1, 1)
        self.pushButton_ComparisonAdd = QtWidgets.QPushButton(self.tab_comparision)
        self.pushButton_ComparisonAdd.setObjectName("pushButton_ComparisonAdd")
        self.gridLayout_3.addWidget(self.pushButton_ComparisonAdd, 1, 0, 1, 1)
        self.gridLayout_4.addLayout(self.gridLayout_3, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_comparision, "")
        self.horizontalLayout_6.addWidget(self.tabWidget)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.pushButton_plot = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_plot.sizePolicy().hasHeightForWidth())
        self.pushButton_plot.setSizePolicy(sizePolicy)
        self.pushButton_plot.setObjectName("pushButton_plot")
        self.verticalLayout_6.addWidget(self.pushButton_plot)
        self.pushButton_clearPlot = QtWidgets.QPushButton(self.widget_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_clearPlot.sizePolicy().hasHeightForWidth())
        self.pushButton_clearPlot.setSizePolicy(sizePolicy)
        self.pushButton_clearPlot.setObjectName("pushButton_clearPlot")
        self.verticalLayout_6.addWidget(self.pushButton_clearPlot)
        self.verticalLayout_7.addLayout(self.verticalLayout_6)
        self.horizontalLayout_6.addWidget(self.widget_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.horizontalLayout_6.addLayout(self.horizontalLayout_5)
        self.verticalLayout_2.addWidget(self.widget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1260, 18))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuTools = QtWidgets.QMenu(self.menubar)
        self.menuTools.setObjectName("menuTools")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.statusbar.sizePolicy().hasHeightForWidth())
        self.statusbar.setSizePolicy(sizePolicy)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.dockWidget_1 = QtWidgets.QDockWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dockWidget_1.sizePolicy().hasHeightForWidth())
        self.dockWidget_1.setSizePolicy(sizePolicy)
        self.dockWidget_1.setObjectName("dockWidget_1")
        self.dockWidgetContents_1 = QtWidgets.QWidget()
        self.dockWidgetContents_1.setObjectName("dockWidgetContents_1")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.dockWidgetContents_1)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.treeView = QtWidgets.QTreeView(self.dockWidgetContents_1)
        self.treeView.setObjectName("treeView")
        self.verticalLayout_5.addWidget(self.treeView)
        self.pushButton_loadFile = QtWidgets.QPushButton(self.dockWidgetContents_1)
        self.pushButton_loadFile.setObjectName("pushButton_loadFile")
        self.verticalLayout_5.addWidget(self.pushButton_loadFile)
        self.pushButton_clearFile = QtWidgets.QPushButton(self.dockWidgetContents_1)
        self.pushButton_clearFile.setObjectName("pushButton_clearFile")
        self.verticalLayout_5.addWidget(self.pushButton_clearFile)
        self.verticalLayout_3.addLayout(self.verticalLayout_5)
        self.dockWidget_1.setWidget(self.dockWidgetContents_1)
        MainWindow.addDockWidget(QtCore.Qt.DockWidgetArea(1), self.dockWidget_1)
        self.actionFilesystem_tree = QtWidgets.QAction(MainWindow)
        self.actionFilesystem_tree.setCheckable(True)
        self.actionFilesystem_tree.setChecked(True)
        self.actionFilesystem_tree.setEnabled(True)
        self.actionFilesystem_tree.setObjectName("actionFilesystem_tree")
        self.actionOpen = QtWidgets.QAction(MainWindow)
        self.actionOpen.setObjectName("actionOpen")
        self.actionData = QtWidgets.QAction(MainWindow)
        self.actionData.setObjectName("actionData")
        self.actionSave_2 = QtWidgets.QAction(MainWindow)
        self.actionSave_2.setObjectName("actionSave_2")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.actionSave_2)
        self.menuFile.addAction(self.actionExit)
        self.menuTools.addAction(self.actionFilesystem_tree)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuTools.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Data Viewer"))
        self.label.setText(_translate("MainWindow", "Method"))
        self.label_2.setText(_translate("MainWindow", "x-axis"))
        self.label_3.setText(_translate("MainWindow", "y-axis"))
        self.label_4.setText(_translate("MainWindow", "Parameters"))
        self.pushButton_AnalysisCompute.setText(_translate("MainWindow", "Compute"))
        self.toolButtonAnalysisParameters.setText(_translate("MainWindow", "..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_analysis), _translate("MainWindow", "Analysis"))
        self.label_7.setText(_translate("MainWindow", "Parameters"))
        self.label_6.setText(_translate("MainWindow", "y-axis"))
        self.toolButtonComparisoParameters.setText(_translate("MainWindow", "..."))
        self.label_5.setText(_translate("MainWindow", "x-axis"))
        self.label_11.setText(_translate("MainWindow", "Measurement"))
        self.pushButton_ComparisonAdd.setText(_translate("MainWindow", "Add from file"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_comparision), _translate("MainWindow", "Comparison"))
        self.pushButton_plot.setText(_translate("MainWindow", "Plot"))
        self.pushButton_clearPlot.setText(_translate("MainWindow", "Clear"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuTools.setTitle(_translate("MainWindow", "Tools"))
        self.pushButton_loadFile.setText(_translate("MainWindow", "Load File"))
        self.pushButton_clearFile.setText(_translate("MainWindow", "Clear "))
        self.actionFilesystem_tree.setText(_translate("MainWindow", "View Filesystem tree"))
        self.actionOpen.setText(_translate("MainWindow", "Open"))
        self.actionOpen.setShortcut(_translate("MainWindow", "Ctrl+O"))
        self.actionData.setText(_translate("MainWindow", "Data"))
        self.actionSave_2.setText(_translate("MainWindow", "Save"))
        self.actionSave_2.setShortcut(_translate("MainWindow", "Ctrl+S"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))
        self.actionExit.setShortcut(_translate("MainWindow", "Ctrl+D"))
from ThermalConductivity.Gui.Widgets.mplwidget import MplWidget
