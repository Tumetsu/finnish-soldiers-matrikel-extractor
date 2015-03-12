# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Thu Mar 12 13:50:11 2015
#      by: PyQt5 UI code generator 5.4
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1123, 694)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.entriesFrame = QtWidgets.QFrame(self.centralwidget)
        self.entriesFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.entriesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.entriesFrame.setObjectName("entriesFrame")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.entriesFrame)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.entriesControlLayout = QtWidgets.QFormLayout()
        self.entriesControlLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.entriesControlLayout.setObjectName("entriesControlLayout")
        self.entriesLabel = QtWidgets.QLabel(self.entriesFrame)
        self.entriesLabel.setObjectName("entriesLabel")
        self.entriesControlLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.entriesLabel)
        self.entriesComboBox = QtWidgets.QComboBox(self.entriesFrame)
        self.entriesComboBox.setMaxVisibleItems(20)
        self.entriesComboBox.setObjectName("entriesComboBox")
        self.entriesComboBox.addItem("")
        self.entriesControlLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.entriesComboBox)
        self.verticalLayout_4.addLayout(self.entriesControlLayout)
        self.entriestListView = EntriesListView(self.entriesFrame)
        self.entriestListView.setStyleSheet("QListWidget {\n"
"alternate-background-color: #EDEDED;\n"
"background-color: white;\n"
"}")
        self.entriestListView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.entriestListView.setAlternatingRowColors(True)
        self.entriestListView.setObjectName("entriestListView")
        self.verticalLayout_4.addWidget(self.entriestListView)
        self.gridLayout.addWidget(self.entriesFrame, 0, 0, 1, 1)
        self.attributesFrame = QtWidgets.QFrame(self.centralwidget)
        self.attributesFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.attributesFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.attributesFrame.setObjectName("attributesFrame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.attributesFrame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.attributesControlsLayout = QtWidgets.QHBoxLayout()
        self.attributesControlsLayout.setObjectName("attributesControlsLayout")
        self.attributesLabel = QtWidgets.QLabel(self.attributesFrame)
        self.attributesLabel.setObjectName("attributesLabel")
        self.attributesControlsLayout.addWidget(self.attributesLabel)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.attributesControlsLayout.addItem(spacerItem)
        self.toolButton = QtWidgets.QToolButton(self.attributesFrame)
        self.toolButton.setStyleSheet("")
        self.toolButton.setObjectName("toolButton")
        self.attributesControlsLayout.addWidget(self.toolButton)
        self.verticalLayout.addLayout(self.attributesControlsLayout)
        self.tableView = EntryTableView(self.attributesFrame)
        self.tableView.setAlternatingRowColors(True)
        self.tableView.setSortingEnabled(True)
        self.tableView.setObjectName("tableView")
        self.tableView.horizontalHeader().setCascadingSectionResizes(False)
        self.tableView.horizontalHeader().setStretchLastSection(False)
        self.verticalLayout.addWidget(self.tableView)
        self.gridLayout.addWidget(self.attributesFrame, 1, 0, 1, 1)
        self.currentFrame = QtWidgets.QFrame(self.centralwidget)
        self.currentFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.currentFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.currentFrame.setObjectName("currentFrame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.currentFrame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.rawTextLabel = QtWidgets.QLabel(self.currentFrame)
        self.rawTextLabel.setObjectName("rawTextLabel")
        self.horizontalLayout.addWidget(self.rawTextLabel)
        self.rawTextCurrentLabel = QtWidgets.QLabel(self.currentFrame)
        self.rawTextCurrentLabel.setText("")
        self.rawTextCurrentLabel.setObjectName("rawTextCurrentLabel")
        self.horizontalLayout.addWidget(self.rawTextCurrentLabel)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.combineButton = QtWidgets.QToolButton(self.currentFrame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combineButton.sizePolicy().hasHeightForWidth())
        self.combineButton.setSizePolicy(sizePolicy)
        self.combineButton.setAutoFillBackground(False)
        self.combineButton.setStyleSheet("")
        self.combineButton.setObjectName("combineButton")
        self.horizontalLayout.addWidget(self.combineButton)
        self.rawTextSaveButton = QtWidgets.QToolButton(self.currentFrame)
        self.rawTextSaveButton.setStyleSheet("")
        self.rawTextSaveButton.setObjectName("rawTextSaveButton")
        self.horizontalLayout.addWidget(self.rawTextSaveButton)
        self.rawTextDeleteButton = QtWidgets.QToolButton(self.currentFrame)
        self.rawTextDeleteButton.setStyleSheet("")
        self.rawTextDeleteButton.setObjectName("rawTextDeleteButton")
        self.horizontalLayout.addWidget(self.rawTextDeleteButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.rawTextTextEdit = QtWidgets.QPlainTextEdit(self.currentFrame)
        self.rawTextTextEdit.setObjectName("rawTextTextEdit")
        self.verticalLayout_2.addWidget(self.rawTextTextEdit)
        self.gridLayout.addWidget(self.currentFrame, 1, 1, 1, 1)
        self.previousFrame = QtWidgets.QFrame(self.centralwidget)
        self.previousFrame.setFrameShape(QtWidgets.QFrame.Panel)
        self.previousFrame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.previousFrame.setObjectName("previousFrame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.previousFrame)
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 12)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.previousControlsLayout = QtWidgets.QHBoxLayout()
        self.previousControlsLayout.setSpacing(2)
        self.previousControlsLayout.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.previousControlsLayout.setContentsMargins(-1, -1, -1, 0)
        self.previousControlsLayout.setObjectName("previousControlsLayout")
        self.previousEntryLabel = QtWidgets.QLabel(self.previousFrame)
        self.previousEntryLabel.setObjectName("previousEntryLabel")
        self.previousControlsLayout.addWidget(self.previousEntryLabel)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.previousControlsLayout.addItem(spacerItem2)
        self.previousENtrySaveButton = QtWidgets.QToolButton(self.previousFrame)
        self.previousENtrySaveButton.setStyleSheet("")
        self.previousENtrySaveButton.setObjectName("previousENtrySaveButton")
        self.previousControlsLayout.addWidget(self.previousENtrySaveButton)
        self.previousEntryDeleteButton = QtWidgets.QToolButton(self.previousFrame)
        self.previousEntryDeleteButton.setStyleSheet("")
        self.previousEntryDeleteButton.setObjectName("previousEntryDeleteButton")
        self.previousControlsLayout.addWidget(self.previousEntryDeleteButton)
        self.verticalLayout_3.addLayout(self.previousControlsLayout)
        self.previousEntryTextEdit = QtWidgets.QPlainTextEdit(self.previousFrame)
        self.previousEntryTextEdit.setObjectName("previousEntryTextEdit")
        self.verticalLayout_3.addWidget(self.previousEntryTextEdit)
        self.gridLayout.addWidget(self.previousFrame, 0, 1, 1, 1)
        self.horizontalLayout_2.addLayout(self.gridLayout)
        self.treeView = EntryTreeView(self.centralwidget)
        self.treeView.setMinimumSize(QtCore.QSize(631, 0))
        self.treeView.setMaximumSize(QtCore.QSize(631, 16777215))
        self.treeView.setUniformRowHeights(True)
        self.treeView.setSortingEnabled(True)
        self.treeView.setAnimated(True)
        self.treeView.setWordWrap(True)
        self.treeView.setExpandsOnDoubleClick(False)
        self.treeView.setObjectName("treeView")
        self.treeView.header().setCascadingSectionResizes(True)
        self.treeView.header().setDefaultSectionSize(100)
        self.treeView.header().setHighlightSections(True)
        self.treeView.header().setMinimumSectionSize(399)
        self.treeView.header().setStretchLastSection(True)
        self.horizontalLayout_2.addWidget(self.treeView)
        self.verticalLayout_5.addLayout(self.horizontalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1123, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuExport = QtWidgets.QMenu(self.menuFile)
        self.menuExport.setObjectName("menuExport")
        self.menuImport = QtWidgets.QMenu(self.menuFile)
        self.menuImport.setObjectName("menuImport")
        self.menuQuit = QtWidgets.QMenu(self.menubar)
        self.menuQuit.setObjectName("menuQuit")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QtWidgets.QToolBar(MainWindow)
        self.toolBar.setObjectName("toolBar")
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionOpen_XML_for_analyze = QtWidgets.QAction(MainWindow)
        self.actionOpen_XML_for_analyze.setObjectName("actionOpen_XML_for_analyze")
        self.actionCsv = QtWidgets.QAction(MainWindow)
        self.actionCsv.setObjectName("actionCsv")
        self.actionJSON = QtWidgets.QAction(MainWindow)
        self.actionJSON.setObjectName("actionJSON")
        self.actionOpen_txt = QtWidgets.QAction(MainWindow)
        self.actionOpen_txt.setObjectName("actionOpen_txt")
        self.actionSave_changes_to_xml = QtWidgets.QAction(MainWindow)
        self.actionSave_changes_to_xml.setObjectName("actionSave_changes_to_xml")
        self.actionFrom_txt_OCR = QtWidgets.QAction(MainWindow)
        self.actionFrom_txt_OCR.setObjectName("actionFrom_txt_OCR")
        self.actionRun_analysis_for_all = QtWidgets.QAction(MainWindow)
        self.actionRun_analysis_for_all.setObjectName("actionRun_analysis_for_all")
        self.actionRun_analysis_for_current = QtWidgets.QAction(MainWindow)
        self.actionRun_analysis_for_current.setObjectName("actionRun_analysis_for_current")
        self.actionCreate_a_new_Person = QtWidgets.QAction(MainWindow)
        self.actionCreate_a_new_Person.setObjectName("actionCreate_a_new_Person")
        self.menuExport.addAction(self.actionCsv)
        self.menuExport.addAction(self.actionJSON)
        self.menuImport.addAction(self.actionFrom_txt_OCR)
        self.menuFile.addAction(self.actionOpen_XML_for_analyze)
        self.menuFile.addAction(self.actionSave_changes_to_xml)
        self.menuFile.addAction(self.menuExport.menuAction())
        self.menuFile.addAction(self.menuImport.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuQuit.menuAction())
        self.toolBar.addAction(self.actionRun_analysis_for_all)
        self.toolBar.addAction(self.actionCreate_a_new_Person)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.entriesLabel.setText(_translate("MainWindow", "Entries "))
        self.entriesComboBox.setItemText(0, _translate("MainWindow", "All"))
        self.attributesLabel.setText(_translate("MainWindow", "Found attributes of entry "))
        self.toolButton.setToolTip(_translate("MainWindow", "<html><head/><body><p>Run extraction for current entry and update attributes. Handy for testing if rawtext editing has helped.</p></body></html>"))
        self.toolButton.setText(_translate("MainWindow", "Rerun analysis"))
        self.rawTextLabel.setText(_translate("MainWindow", "Rawtext "))
        self.combineButton.setText(_translate("MainWindow", "Combine"))
        self.rawTextSaveButton.setText(_translate("MainWindow", "Save"))
        self.rawTextDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.previousEntryLabel.setText(_translate("MainWindow", "Previous entry"))
        self.previousENtrySaveButton.setText(_translate("MainWindow", "Save"))
        self.previousEntryDeleteButton.setText(_translate("MainWindow", "Delete"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.menuExport.setTitle(_translate("MainWindow", "Export"))
        self.menuImport.setTitle(_translate("MainWindow", "Import"))
        self.menuQuit.setTitle(_translate("MainWindow", "Quit"))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar"))
        self.actionOpen_XML_for_analyze.setText(_translate("MainWindow", "Open xml"))
        self.actionCsv.setText(_translate("MainWindow", "CSV"))
        self.actionJSON.setText(_translate("MainWindow", "JSON"))
        self.actionOpen_txt.setText(_translate("MainWindow", "Open txt"))
        self.actionSave_changes_to_xml.setText(_translate("MainWindow", "Save changes to xml"))
        self.actionFrom_txt_OCR.setText(_translate("MainWindow", "From txt (OCR)"))
        self.actionRun_analysis_for_all.setText(_translate("MainWindow", "Run analysis for all"))
        self.actionRun_analysis_for_all.setToolTip(_translate("MainWindow", "Run analysis for all entries in current file"))
        self.actionRun_analysis_for_all.setShortcut(_translate("MainWindow", "Ctrl+Shift+R"))
        self.actionRun_analysis_for_current.setText(_translate("MainWindow", "Run analysis for current"))
        self.actionRun_analysis_for_current.setToolTip(_translate("MainWindow", "Run extraction for current person and update attributes"))
        self.actionRun_analysis_for_current.setShortcut(_translate("MainWindow", "Ctrl+R"))
        self.actionCreate_a_new_Person.setText(_translate("MainWindow", "Create a  new Person"))
        self.actionCreate_a_new_Person.setToolTip(_translate("MainWindow", "Create a new person from rawtext"))

from qtgui.entrytable import EntryTableView
from qtgui.entrytree import EntryTreeView
from qtgui.entriesModels import EntriesListView
