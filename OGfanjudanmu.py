# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'OGfanjudanmu.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1041, 714)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(2)
        sizePolicy.setVerticalStretch(5)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setObjectName("groupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.groupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.frame_6 = QtWidgets.QFrame(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy)
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.formLayout = QtWidgets.QFormLayout(self.frame_6)
        self.formLayout.setFieldGrowthPolicy(QtWidgets.QFormLayout.AllNonFixedFieldsGrow)
        self.formLayout.setVerticalSpacing(20)
        self.formLayout.setObjectName("formLayout")
        self.label_1 = QtWidgets.QLabel(self.frame_6)
        self.label_1.setObjectName("label_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_1)
        self.lineEdit_1 = QtWidgets.QLineEdit(self.frame_6)
        self.lineEdit_1.setObjectName("lineEdit_1")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_1)
        self.label = QtWidgets.QLabel(self.frame_6)
        self.label.setObjectName("label")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label)
        self.textBrowser = QtWidgets.QTextBrowser(self.frame_6)
        self.textBrowser.setEnabled(True)
        self.textBrowser.setObjectName("textBrowser")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textBrowser)
        self.label_4 = QtWidgets.QLabel(self.frame_6)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setContentsMargins(5, 5, 5, 5)
        self.horizontalLayout_8.setSpacing(15)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.spinBox_3 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_3.setObjectName("spinBox_3")
        self.horizontalLayout_8.addWidget(self.spinBox_3)
        self.label_10 = QtWidgets.QLabel(self.frame_6)
        self.label_10.setObjectName("label_10")
        self.horizontalLayout_8.addWidget(self.label_10)
        self.spinBox_4 = QtWidgets.QSpinBox(self.frame_6)
        self.spinBox_4.setObjectName("spinBox_4")
        self.horizontalLayout_8.addWidget(self.spinBox_4)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem)
        self.formLayout.setLayout(4, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout_8)
        self.label_5 = QtWidgets.QLabel(self.frame_6)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.pushButton_8 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_8.setObjectName("pushButton_8")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.pushButton_8)
        self.label_6 = QtWidgets.QLabel(self.frame_6)
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.pushButton_9 = QtWidgets.QPushButton(self.frame_6)
        self.pushButton_9.setObjectName("pushButton_9")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.FieldRole, self.pushButton_9)
        self.verticalLayout_4.addWidget(self.frame_6)
        self.frame_4 = QtWidgets.QFrame(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.textBrowser_1 = QtWidgets.QTextBrowser(self.frame_4)
        self.textBrowser_1.setObjectName("textBrowser_1")
        self.verticalLayout_5.addWidget(self.textBrowser_1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.pushButton_1 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_1.setObjectName("pushButton_1")
        self.horizontalLayout_4.addWidget(self.pushButton_1)
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_4.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame_4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_4.addWidget(self.pushButton_3)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_4.addWidget(self.frame_4)
        self.horizontalLayout.addWidget(self.groupBox)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(5)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        # self.tableView = QtWidgets.QTableView(self.frame_2)
        # self.tableView.setObjectName("tableView")
        # self.horizontalLayout_3.addWidget(self.tableView)
        self.verticalLayout.addWidget(self.frame_2)
        self.line = QtWidgets.QFrame(self.frame)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout.addWidget(self.line)
        self.frame_3 = QtWidgets.QFrame(self.frame)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.frame_3)
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.verticalLayout_2.addWidget(self.textBrowser_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_2.addWidget(self.pushButton_4)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_2.addWidget(self.pushButton_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame_3)
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        spacerItem3 = QtWidgets.QSpacerItem(168, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame_3)
        self.horizontalLayout.addWidget(self.frame)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1041, 26))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_4 = QtWidgets.QAction(MainWindow)
        self.action_4.setObjectName("action_4")
        self.menu.addAction(self.action)
        self.menu_2.addAction(self.action_4)
        self.menu_3.addAction(self.action_2)
        self.menu_3.addAction(self.action_3)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "bilibili番剧弹幕"))
        self.label_1.setText(_translate("MainWindow", "番剧ep号："))
        self.label.setText(_translate("MainWindow", "导入提示："))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">1.请确保文件后缀为(.xls)，且文件能够打开</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">2.番剧ep号为一部番剧任意一集网址最后的数字，如点兔第一集第一集网址https://www.bilibili.com/bangumi/play/ep95840?from=search&seid=12453105052239622776，则ep号为ep后面的数字：95840\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">3.请确保第一列全为ep号（纯数字）。不能为ep:123123</p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">4.每一集弹幕最大量为3000，excel文件最多支持65000行，所以能爬取18集以下的番剧（虽然一般是12集），对与半年番（大于18集）请麻烦分集爬取。</p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "搜索集数："))
        self.label_10.setText(_translate("MainWindow", "至"))
        self.label_5.setText(_translate("MainWindow", "导入文件："))
        self.pushButton_8.setText(_translate("MainWindow", "点击选择"))
        self.label_6.setText(_translate("MainWindow", "导出文件："))
        self.pushButton_9.setText(_translate("MainWindow", "点击选择"))
        self.pushButton_1.setText(_translate("MainWindow", "检查参数"))
        self.pushButton_2.setText(_translate("MainWindow", "清空参数"))
        self.pushButton_3.setText(_translate("MainWindow", "清空提示窗口"))
        self.pushButton_4.setText(_translate("MainWindow", "开始"))
        self.pushButton_5.setText(_translate("MainWindow", "中止"))
        self.pushButton_6.setText(_translate("MainWindow", "导出至Excel"))
        self.menu.setTitle(_translate("MainWindow", "数据库"))
        self.menu_2.setTitle(_translate("MainWindow", "帮助"))
        self.menu_3.setTitle(_translate("MainWindow", "关于"))
        self.action.setText(_translate("MainWindow", "连接数据库（待开发）"))
        self.action_2.setText(_translate("MainWindow", "版本"))
        self.action_3.setText(_translate("MainWindow", "制作人"))
        self.action_4.setText(_translate("MainWindow", "联系我们"))

