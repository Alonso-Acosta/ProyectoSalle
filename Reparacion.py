# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Reparacion.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc

class Ui_Form2(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1250, 750)
        self.tabWidget = QTabWidget(Form)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 1250, 750))
        self.tabWidget.setStyleSheet(u"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}\n"
"QTabWidget{\n"
"Border: 1px solid #003057;\n"
"}")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.frame = QFrame(self.tab)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 1243, 461))
        font = QFont()
        font.setFamilies([u"Arial"])
        self.frame.setFont(font)
        self.frame.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget = QWidget(self.frame)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(50, 50, 381, 191))
        self.gridLayout_2 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.label_8 = QLabel(self.gridLayoutWidget)
        self.label_8.setObjectName(u"label_8")
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(8)
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_2.addWidget(self.label_8, 1, 0, 1, 1)

        self.label_9 = QLabel(self.gridLayoutWidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font1)
        self.label_9.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)

        self.dateEdit = QDateEdit(self.gridLayoutWidget)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setMinimumSize(QSize(0, 35))
        self.dateEdit.setFont(font)
        self.dateEdit.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_2.addWidget(self.dateEdit, 1, 1, 1, 1)

        self.dateEdit_3 = QDateEdit(self.gridLayoutWidget)
        self.dateEdit_3.setObjectName(u"dateEdit_3")
        self.dateEdit_3.setMinimumSize(QSize(0, 35))
        self.dateEdit_3.setFont(font)
        self.dateEdit_3.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_3.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_3.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_2.addWidget(self.dateEdit_3, 2, 1, 1, 1)

        self.lineEdit = QLineEdit(self.gridLayoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(0, 35))
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet(u"")

        self.gridLayout_2.addWidget(self.lineEdit, 0, 1, 1, 1)

        self.label = QLabel(self.gridLayoutWidget)
        self.label.setObjectName(u"label")
        self.label.setFont(font1)
        self.label.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_2.addWidget(self.label, 0, 0, 1, 1)

        self.label_2 = QLabel(self.gridLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_2.addWidget(self.label_2, 0, 4, 1, 1)

        self.textEdit = QTextEdit(self.frame)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(440, 60, 311, 161))
        self.textEdit.setFont(font)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"background: #FBD27E;\n"
"}")
        self.gridLayoutWidget_3 = QWidget(self.frame)
        self.gridLayoutWidget_3.setObjectName(u"gridLayoutWidget_3")
        self.gridLayoutWidget_3.setGeometry(QRect(760, 60, 341, 114))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_6 = QLabel(self.gridLayoutWidget_3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_6 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMinimumSize(QSize(0, 35))
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_6, 1, 1, 1, 1)

        self.lineEdit_3 = QLineEdit(self.gridLayoutWidget_3)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setMinimumSize(QSize(0, 35))
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_3, 0, 1, 1, 1)

        self.label_3 = QLabel(self.gridLayoutWidget_3)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout.addWidget(self.label_3, 0, 0, 1, 1)

        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(1120, 75, 41, 28))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon = QIcon()
        icon.addFile(u":/Icon/Recursos/Profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 23))
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(1120, 125, 41, 28))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/Icon/Recursos/IDM.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(30, 30))
        self.pushButton_18 = QPushButton(self.frame)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setGeometry(QRect(1105, 300, 101, 31))
        palette = QPalette()
        brush = QBrush(QColor(0, 48, 87, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(255, 255, 255, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(0, 72, 131, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(0, 60, 109, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        brush4 = QBrush(QColor(0, 24, 43, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush4)
        brush5 = QBrush(QColor(0, 32, 58, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Active, QPalette.Text, brush)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Active, QPalette.Window, brush1)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        brush7 = QBrush(QColor(255, 255, 220, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_18.setPalette(palette)
        font2 = QFont()
        font2.setFamilies([u"Montserrat"])
        font2.setPointSize(8)
        self.pushButton_18.setFont(font2)
        self.pushButton_18.setMouseTracking(False)
        icon2 = QIcon()
        icon2.addFile(u":/Icon/Recursos/Registrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_18.setIcon(icon2)
        self.pushButton_18.setIconSize(QSize(100, 44))
        self.pushButton_18.setAutoDefault(False)
        self.pushButton_19 = QPushButton(self.frame)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setGeometry(QRect(1105, 360, 100, 30))
        font3 = QFont()
        font3.setFamilies([u"Montserrat"])
        self.pushButton_19.setFont(font3)
        self.pushButton_19.setMouseTracking(False)
        icon3 = QIcon()
        icon3.addFile(u":/Icon/Recursos/Modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_19.setIcon(icon3)
        self.pushButton_19.setIconSize(QSize(100, 44))
        self.pushButton_19.setAutoDefault(False)
        self.tableWidget_3 = QTableWidget(self.frame)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setGeometry(QRect(30, 260, 1021, 181))
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(145)
        self.pushButton_22 = QPushButton(self.frame)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(1070, 260, 31, 31))
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush)
        palette1.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette1.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette1.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette1.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_22.setPalette(palette1)
        self.pushButton_22.setFont(font2)
        self.pushButton_22.setMouseTracking(False)
        self.pushButton_22.setIconSize(QSize(100, 44))
        self.pushButton_22.setAutoDefault(False)
        self.widget = QWidget(self.tab)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 470, 1243, 251))
        self.widget.setStyleSheet(u"QWidget{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}\n"
"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}\n"
"")
        self.label_10 = QLabel(self.widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(30, 20, 151, 16))
        font4 = QFont()
        font4.setFamilies([u"Arial"])
        font4.setPointSize(10)
        self.label_10.setFont(font4)
        self.label_10.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.label_11 = QLabel(self.widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(850, 66, 111, 35))
        self.label_11.setFont(font1)
        self.label_11.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBox_2 = QComboBox(self.widget)
        self.comboBox_2.addItem("")
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBox_2.setMinimumSize(QSize(181, 35))
        font5 = QFont()
        font5.setFamilies([u"Arial"])
        font5.setStyleStrategy(QFont.PreferDefault)
        self.comboBox_2.setFont(font5)
        self.comboBox_2.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBox_2.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_2.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_2.setFrame(False)
        self.label_12 = QLabel(self.widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(850, 136, 45, 35))
        self.label_12.setFont(font1)
        self.label_12.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_5 = QLineEdit(self.widget)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_5.setMinimumSize(QSize(0, 35))
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet(u"")
        self.pushButton_12 = QPushButton(self.widget)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(1270, 200, 104, 31))
        self.pushButton_12.setMouseTracking(False)
        self.pushButton_12.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u":/Icon/Componente 29 \u2013 6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_12.setIcon(icon4)
        self.pushButton_12.setIconSize(QSize(100, 31))
        self.pushButton_12.setAutoDefault(False)
        self.pushButton_13 = QPushButton(self.widget)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(1440, 200, 104, 31))
        self.pushButton_13.setMouseTracking(False)
        self.pushButton_13.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon5 = QIcon()
        icon5.addFile(u":/Icon/Componente 28 \u2013 6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_13.setIcon(icon5)
        self.pushButton_13.setIconSize(QSize(101, 35))
        self.pushButton_13.setAutoDefault(False)
        self.pushButton_5 = QPushButton(self.widget)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_5.setFont(font3)
        icon6 = QIcon()
        icon6.addFile(u":/Icon/Recursos/Eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon6)
        self.pushButton_6 = QPushButton(self.widget)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_6.setFont(font3)
        icon7 = QIcon()
        icon7.addFile(u":/Icon/Recursos/Consultar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon7)
        self.tableWidget_4 = QTableWidget(self.widget)
        if (self.tableWidget_4.columnCount() < 7):
            self.tableWidget_4.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget_4.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.tableWidget_4.setObjectName(u"tableWidget_4")
        self.tableWidget_4.setGeometry(QRect(20, 50, 810, 180))
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.frame_2 = QFrame(self.tab_2)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 1243, 461))
        self.frame_2.setFont(font)
        self.frame_2.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_2.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_2 = QWidget(self.frame_2)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(50, 50, 381, 191))
        self.gridLayout_3 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.label_13 = QLabel(self.gridLayoutWidget_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font1)
        self.label_13.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_3.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_14 = QLabel(self.gridLayoutWidget_2)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font1)
        self.label_14.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_3.addWidget(self.label_14, 2, 0, 1, 1)

        self.dateEdit_2 = QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_2.setObjectName(u"dateEdit_2")
        self.dateEdit_2.setMinimumSize(QSize(0, 35))
        self.dateEdit_2.setFont(font)
        self.dateEdit_2.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_2.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_2.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_3.addWidget(self.dateEdit_2, 1, 1, 1, 1)

        self.dateEdit_4 = QDateEdit(self.gridLayoutWidget_2)
        self.dateEdit_4.setObjectName(u"dateEdit_4")
        self.dateEdit_4.setMinimumSize(QSize(0, 35))
        self.dateEdit_4.setFont(font)
        self.dateEdit_4.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_4.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_4.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_3.addWidget(self.dateEdit_4, 2, 1, 1, 1)

        self.lineEdit_2 = QLineEdit(self.gridLayoutWidget_2)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(0, 35))
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet(u"")

        self.gridLayout_3.addWidget(self.lineEdit_2, 0, 1, 1, 1)

        self.label_4 = QLabel(self.gridLayoutWidget_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_3.addWidget(self.label_4, 0, 0, 1, 1)

        self.label_5 = QLabel(self.gridLayoutWidget_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_3.addWidget(self.label_5, 0, 4, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_2)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(440, 60, 311, 161))
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"background: #FBD27E;\n"
"}")
        self.gridLayoutWidget_4 = QWidget(self.frame_2)
        self.gridLayoutWidget_4.setObjectName(u"gridLayoutWidget_4")
        self.gridLayoutWidget_4.setGeometry(QRect(760, 60, 341, 114))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_7 = QLabel(self.gridLayoutWidget_4)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_4.addWidget(self.label_7, 1, 0, 1, 1)

        self.lineEdit_7 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_7.setObjectName(u"lineEdit_7")
        self.lineEdit_7.setMinimumSize(QSize(0, 35))
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_7, 1, 1, 1, 1)

        self.lineEdit_4 = QLineEdit(self.gridLayoutWidget_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMinimumSize(QSize(0, 35))
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet(u"")

        self.gridLayout_4.addWidget(self.lineEdit_4, 0, 1, 1, 1)

        self.label_15 = QLabel(self.gridLayoutWidget_4)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font1)
        self.label_15.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_4.addWidget(self.label_15, 0, 0, 1, 1)

        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(1120, 75, 41, 28))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(30, 23))
        self.pushButton_4 = QPushButton(self.frame_2)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(1120, 125, 41, 28))
        self.pushButton_4.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_4.setIcon(icon1)
        self.pushButton_4.setIconSize(QSize(30, 30))
        self.pushButton_20 = QPushButton(self.frame_2)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(1105, 300, 101, 31))
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush)
        palette2.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette2.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette2.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette2.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette2.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_20.setPalette(palette2)
        self.pushButton_20.setFont(font2)
        self.pushButton_20.setMouseTracking(False)
        self.pushButton_20.setIcon(icon2)
        self.pushButton_20.setIconSize(QSize(100, 44))
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_21 = QPushButton(self.frame_2)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(1105, 360, 100, 30))
        self.pushButton_21.setFont(font3)
        self.pushButton_21.setMouseTracking(False)
        self.pushButton_21.setIcon(icon3)
        self.pushButton_21.setIconSize(QSize(100, 44))
        self.pushButton_21.setAutoDefault(False)
        self.tableWidget = QTableWidget(self.frame_2)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(30, 260, 1021, 181))
        self.pushButton_23 = QPushButton(self.frame_2)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setGeometry(QRect(1060, 270, 31, 31))
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_23.setPalette(palette3)
        self.pushButton_23.setFont(font2)
        self.pushButton_23.setMouseTracking(False)
        self.pushButton_23.setIconSize(QSize(100, 44))
        self.pushButton_23.setAutoDefault(False)
        self.widget_2 = QWidget(self.tab_2)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setGeometry(QRect(0, 470, 1243, 251))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}\n"
"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}")
        self.label_16 = QLabel(self.widget_2)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(30, 20, 151, 16))
        self.label_16.setFont(font4)
        self.label_16.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.pushButton_16 = QPushButton(self.widget_2)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setGeometry(QRect(1290, 210, 101, 31))
        self.pushButton_16.setMouseTracking(False)
        self.pushButton_16.setIcon(icon4)
        self.pushButton_16.setIconSize(QSize(100, 31))
        self.pushButton_16.setAutoDefault(False)
        self.pushButton_17 = QPushButton(self.widget_2)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setGeometry(QRect(1410, 210, 101, 31))
        self.pushButton_17.setMouseTracking(False)
        self.pushButton_17.setIcon(icon5)
        self.pushButton_17.setIconSize(QSize(101, 35))
        self.pushButton_17.setAutoDefault(False)
        self.label_22 = QLabel(self.widget_2)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setGeometry(QRect(850, 70, 115, 28))
        self.label_22.setFont(font1)
        self.label_22.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBox_4 = QComboBox(self.widget_2)
        self.comboBox_4.setObjectName(u"comboBox_4")
        self.comboBox_4.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBox_4.setMinimumSize(QSize(181, 35))
        self.comboBox_4.setFont(font5)
        self.comboBox_4.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBox_4.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_4.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_4.setFrame(False)
        self.label_23 = QLabel(self.widget_2)
        self.label_23.setObjectName(u"label_23")
        self.label_23.setGeometry(QRect(850, 140, 45, 28))
        self.label_23.setFont(font1)
        self.label_23.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_11 = QLineEdit(self.widget_2)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_11.setMinimumSize(QSize(0, 35))
        self.lineEdit_11.setFont(font)
        self.lineEdit_11.setStyleSheet(u"")
        self.pushButton_7 = QPushButton(self.widget_2)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_7.setFont(font3)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_8 = QPushButton(self.widget_2)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_8.setFont(font3)
        self.pushButton_8.setIcon(icon7)
        self.tableWidget_2 = QTableWidget(self.widget_2)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(20, 50, 810, 180))
        self.tabWidget.addTab(self.tab_2, "")

        self.retranslateUi(Form)

        self.tabWidget.setCurrentIndex(0)
        self.pushButton_18.setDefault(False)
        self.pushButton_19.setDefault(False)
        self.pushButton_22.setDefault(False)
        self.pushButton_12.setDefault(False)
        self.pushButton_13.setDefault(False)
        self.pushButton_20.setDefault(False)
        self.pushButton_21.setDefault(False)
        self.pushButton_23.setDefault(False)
        self.pushButton_16.setDefault(False)
        self.pushButton_17.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"Fecha De Ingreso:", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"Fecha De Retorno:", None))
        self.dateEdit.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/d", None))
        self.dateEdit_3.setDisplayFormat(QCoreApplication.translate("Form", u"yyyy/MM/d", None))
        self.label.setText(QCoreApplication.translate("Form", u"ID:", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"Descripci\u00f3n:", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"ID Instrumento", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"ID Laboratorista", None))
        self.pushButton.setText("")
        self.pushButton_2.setText("")
        self.pushButton_18.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.pushButton_19.setText(QCoreApplication.translate("Form", u"Modificar", None))
        ___qtablewidgetitem = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem1 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("Form", u"Fecha Ingreso", None));
        ___qtablewidgetitem2 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("Form", u"Fecha Retorno", None));
        ___qtablewidgetitem3 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("Form", u"Descripcion", None));
        ___qtablewidgetitem4 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("Form", u"ID Labaratorista", None));
        ___qtablewidgetitem5 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("Form", u"ID Maquina", None));
        ___qtablewidgetitem6 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("Form", u"ID Instrumento", None));
        self.pushButton_22.setText("")
        self.label_10.setText(QCoreApplication.translate("Form", u"TABLA CONSULTA", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"Filtro De Busqueda", None))
        self.comboBox_2.setItemText(0, "")

        self.label_12.setText(QCoreApplication.translate("Form", u"Buscar:", None))
        self.pushButton_12.setText("")
        self.pushButton_13.setText("")
        self.pushButton_5.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.pushButton_6.setText(QCoreApplication.translate("Form", u"Consultar", None))
        ___qtablewidgetitem7 = self.tableWidget_4.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("Form", u"ID", None));
        ___qtablewidgetitem8 = self.tableWidget_4.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("Form", u"Fecha Ingreso", None));
        ___qtablewidgetitem9 = self.tableWidget_4.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("Form", u"Fecha Retorno", None));
        ___qtablewidgetitem10 = self.tableWidget_4.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("Form", u"Descripcion", None));
        ___qtablewidgetitem11 = self.tableWidget_4.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("Form", u"Nueva columna", None));
        ___qtablewidgetitem12 = self.tableWidget_4.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("Form", u"ID Maquina", None));
        ___qtablewidgetitem13 = self.tableWidget_4.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("Form", u"ID Instrumento", None));
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("Form", u"Instrumetos", None))
        self.label_13.setText(QCoreApplication.translate("Form", u"Fecha De Ingreso:", None))
        self.label_14.setText(QCoreApplication.translate("Form", u"Fecha De Retorno:", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"ID:", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"Desciprcion", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"ID M\u00e1quina", None))
        self.label_15.setText(QCoreApplication.translate("Form", u"ID Laboratorista", None))
        self.pushButton_3.setText("")
        self.pushButton_4.setText("")
        self.pushButton_20.setText(QCoreApplication.translate("Form", u"Registrar", None))
        self.pushButton_21.setText(QCoreApplication.translate("Form", u"Modificar", None))
        self.pushButton_23.setText("")
        self.label_16.setText(QCoreApplication.translate("Form", u"TABLA CONSULTA", None))
        self.pushButton_16.setText("")
        self.pushButton_17.setText("")
        self.label_22.setText(QCoreApplication.translate("Form", u"Filtro De Busqueda:", None))
        self.label_23.setText(QCoreApplication.translate("Form", u"Buscar:", None))
        self.pushButton_7.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.pushButton_8.setText(QCoreApplication.translate("Form", u"Consultar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("Form", u"M\u00e1quinas", None))
    # retranslateUi

