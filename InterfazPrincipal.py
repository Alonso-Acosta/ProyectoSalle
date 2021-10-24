# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Probando.ui'
##
## Created by: Qt User Interface Compiler version 6.1.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

import resources_rc
import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1500, 838)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayoutWidget = QWidget(self.centralwidget)
        self.verticalLayoutWidget.setObjectName(u"verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 1924, 1083))
        self.verticalLayout = QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.verticalLayoutWidget)
        self.widget.setObjectName(u"widget")
        self.widget.setEnabled(True)
        self.widget.setMinimumSize(QSize(1500, 82))
        self.widget.setMaximumSize(QSize(1500, 82))
        self.widget.setStyleSheet(u"QWidget{\n"
"Background: #ffffff;\n"
"}")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 251, 81))
        self.label.setPixmap(QPixmap(u":/Icon/Recursos/lajalle.png"))
        self.label.setScaledContents(True)
        self.formLayoutWidget = QWidget(self.widget)
        self.formLayoutWidget.setObjectName(u"formLayoutWidget")
        self.formLayoutWidget.setGeometry(QRect(1300, 10, 178, 61))
        self.formLayout = QFormLayout(self.formLayoutWidget)
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.label_2 = QLabel(self.formLayoutWidget)
        self.label_2.setObjectName(u"label_2")
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(8)
        font.setBold(True)
        self.label_2.setFont(font)

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.label_2)

        self.label_3 = QLabel(self.formLayoutWidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(60, 50))
        self.label_3.setPixmap(QPixmap(u":/Icon/Recursos/user.png"))
        self.label_3.setScaledContents(True)

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_3)


        self.verticalLayout.addWidget(self.widget)

        self.widget_2 = QWidget(self.verticalLayoutWidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setEnabled(True)
        self.widget_2.setMinimumSize(QSize(1920, 988))
        self.widget_2.setMaximumSize(QSize(1920, 988))
        self.widget_2.setStyleSheet(u"QWidget{\n"
"Background:#ffffff;\n"
"}")
        self.dockWidget_4 = QDockWidget(self.widget_2)
        self.dockWidget_4.setObjectName(u"dockWidget_4")
        self.dockWidget_4.setGeometry(QRect(0, -30, 251, 1015))
        self.dockWidget_4.setMinimumSize(QSize(251, 1015))
        self.dockWidget_4.setAutoFillBackground(False)
        self.dockWidget_4.setStyleSheet(u"QDockWidget{\n"
"background:#ffffff;\n"
"}")
        self.dockWidget_4.setFeatures(QDockWidget.NoDockWidgetFeatures)
        self.dockWidgetContents_3 = QWidget()
        self.dockWidgetContents_3.setObjectName(u"dockWidgetContents_3")
        self.dockWidgetContents_3.setStyleSheet(u"QWidget{\n"
"\n"
"Background:#ffffff;\n"
"}")
        self.pushButton = QPushButton(self.dockWidgetContents_3)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(True)
        self.pushButton.setGeometry(QRect(0, 0, 251, 51))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(9)
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setLayoutDirection(Qt.LeftToRight)
        icon = QIcon()
        icon.addFile(u":/Icon/Recursos/Icon Home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(30, 30))
        self.pushButton_2 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(True)
        self.pushButton_2.setGeometry(QRect(0, 50, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setFont(font1)
        self.pushButton_2.setLayoutDirection(Qt.LeftToRight)
        icon1 = QIcon()
        icon1.addFile(u":/Icon/Recursos/Search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(251, 251))
        self.pushButton_3 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setGeometry(QRect(0, 100, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setFont(font1)
        self.pushButton_3.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/Icon/Recursos/Reparaciones.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QSize(251, 251))
        self.pushButton_4 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setEnabled(True)
        self.pushButton_4.setGeometry(QRect(0, 150, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_4.sizePolicy().hasHeightForWidth())
        self.pushButton_4.setSizePolicy(sizePolicy)
        self.pushButton_4.setFont(font1)
        self.pushButton_4.setLayoutDirection(Qt.LeftToRight)
        icon3 = QIcon()
        icon3.addFile(u":/Icon/Recursos/Mantenimiento.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_4.setIcon(icon3)
        self.pushButton_4.setIconSize(QSize(40, 40))
        self.pushButton_5 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setEnabled(True)
        self.pushButton_5.setGeometry(QRect(0, 200, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_5.sizePolicy().hasHeightForWidth())
        self.pushButton_5.setSizePolicy(sizePolicy)
        self.pushButton_5.setFont(font1)
        self.pushButton_5.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/Icon/Recursos/Pretamos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_5.setIcon(icon4)
        self.pushButton_5.setIconSize(QSize(251, 251))
        self.pushButton_6 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setEnabled(True)
        self.pushButton_6.setGeometry(QRect(0, 250, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_6.sizePolicy().hasHeightForWidth())
        self.pushButton_6.setSizePolicy(sizePolicy)
        self.pushButton_6.setFont(font1)
        self.pushButton_6.setLayoutDirection(Qt.LeftToRight)
        icon5 = QIcon()
        icon5.addFile(u":/Icon/Recursos/Asignacion.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_6.setIcon(icon5)
        self.pushButton_6.setIconSize(QSize(251, 251))
        self.pushButton_7 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setEnabled(True)
        self.pushButton_7.setGeometry(QRect(0, 300, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_7.sizePolicy().hasHeightForWidth())
        self.pushButton_7.setSizePolicy(sizePolicy)
        self.pushButton_7.setFont(font1)
        self.pushButton_7.setLayoutDirection(Qt.LeftToRight)
        icon6 = QIcon()
        icon6.addFile(u":/Icon/Recursos/Consulta.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_7.setIcon(icon6)
        self.pushButton_7.setIconSize(QSize(251, 251))
        self.pushButton_8 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setEnabled(True)
        self.pushButton_8.setGeometry(QRect(0, 350, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_8.sizePolicy().hasHeightForWidth())
        self.pushButton_8.setSizePolicy(sizePolicy)
        self.pushButton_8.setFont(font1)
        self.pushButton_8.setLayoutDirection(Qt.LeftToRight)
        icon7 = QIcon()
        icon7.addFile(u":/Icon/Recursos/Ayuda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_8.setIcon(icon7)
        self.pushButton_8.setIconSize(QSize(251, 251))
        self.pushButton_9 = QPushButton(self.dockWidgetContents_3)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setEnabled(True)
        self.pushButton_9.setGeometry(QRect(0, 400, 251, 51))
        sizePolicy.setHeightForWidth(self.pushButton_9.sizePolicy().hasHeightForWidth())
        self.pushButton_9.setSizePolicy(sizePolicy)
        self.pushButton_9.setFont(font1)
        self.pushButton_9.setLayoutDirection(Qt.LeftToRight)
        icon8 = QIcon()
        icon8.addFile(u":/Icon/Recursos/ajuste.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_9.setIcon(icon8)
        self.pushButton_9.setIconSize(QSize(251, 251))
        self.dockWidget_4.setWidget(self.dockWidgetContents_3)
        self.WCentral = QWidget(self.widget_2)
        self.WCentral.setObjectName(u"WCentral")
        self.WCentral.setGeometry(QRect(250, 0, 1250, 750))
        self.WCentral.setStyleSheet(u"QWidget{\n"
"Background: #ffffff;\n"
"}")
        self.Wreparacion = QWidget(self.WCentral)
        self.Wreparacion.setObjectName(u"Wreparacion")
        self.Wreparacion.setGeometry(QRect(0, 0, 1250, 0))
        self.tabWidget_3 = QTabWidget(self.Wreparacion)
        self.tabWidget_3.setObjectName(u"tabWidget_3")
        self.tabWidget_3.setGeometry(QRect(0, 0, 1250, 750))
        self.tabWidget_3.setStyleSheet(u"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}\n"
"QTabWidget{\n"
"Border: 1px solid #003057;\n"
"}")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.frame_5 = QFrame(self.tab_5)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(0, 0, 1243, 461))
        font2 = QFont()
        font2.setFamilies([u"Arial"])
        self.frame_5.setFont(font2)
        self.frame_5.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_5.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_5 = QWidget(self.frame_5)
        self.gridLayoutWidget_5.setObjectName(u"gridLayoutWidget_5")
        self.gridLayoutWidget_5.setGeometry(QRect(50, 50, 381, 191))
        self.gridLayout_6 = QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_54 = QLabel(self.gridLayoutWidget_5)
        self.label_54.setObjectName(u"label_54")
        font3 = QFont()
        font3.setFamilies([u"Arial"])
        font3.setPointSize(8)
        self.label_54.setFont(font3)
        self.label_54.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_6.addWidget(self.label_54, 1, 0, 1, 1)

        self.label_55 = QLabel(self.gridLayoutWidget_5)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font3)
        self.label_55.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_6.addWidget(self.label_55, 2, 0, 1, 1)

        self.dateEdit_5 = QDateEdit(self.gridLayoutWidget_5)
        self.dateEdit_5.setObjectName(u"dateEdit_5")
        self.dateEdit_5.setMinimumSize(QSize(0, 35))
        self.dateEdit_5.setFont(font2)
        self.dateEdit_5.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_5.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_5.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_6.addWidget(self.dateEdit_5, 1, 1, 1, 1)

        self.dateEdit_6 = QDateEdit(self.gridLayoutWidget_5)
        self.dateEdit_6.setObjectName(u"dateEdit_6")
        self.dateEdit_6.setMinimumSize(QSize(0, 35))
        self.dateEdit_6.setFont(font2)
        self.dateEdit_6.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_6.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_6.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_6.addWidget(self.dateEdit_6, 2, 1, 1, 1)

        self.lineEdit_31 = QLineEdit(self.gridLayoutWidget_5)
        self.lineEdit_31.setObjectName(u"lineEdit_31")
        self.lineEdit_31.setMinimumSize(QSize(0, 35))
        self.lineEdit_31.setFont(font2)
        self.lineEdit_31.setStyleSheet(u"")

        self.gridLayout_6.addWidget(self.lineEdit_31, 0, 1, 1, 1)

        self.label_56 = QLabel(self.gridLayoutWidget_5)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setFont(font3)
        self.label_56.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_6.addWidget(self.label_56, 0, 0, 1, 1)

        self.label_57 = QLabel(self.gridLayoutWidget_5)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font3)
        self.label_57.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_6.addWidget(self.label_57, 0, 4, 1, 1)

        self.textEdit = QTextEdit(self.frame_5)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(440, 60, 311, 161))
        self.textEdit.setFont(font2)
        self.textEdit.setStyleSheet(u"QTextEdit{\n"
"background: #FBD27E;\n"
"}")
        self.gridLayoutWidget_6 = QWidget(self.frame_5)
        self.gridLayoutWidget_6.setObjectName(u"gridLayoutWidget_6")
        self.gridLayoutWidget_6.setGeometry(QRect(760, 60, 341, 114))
        self.gridLayout = QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_58 = QLabel(self.gridLayoutWidget_6)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font3)
        self.label_58.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout.addWidget(self.label_58, 1, 0, 1, 1)

        self.lineEdit_32 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_32.setObjectName(u"lineEdit_32")
        self.lineEdit_32.setMinimumSize(QSize(0, 35))
        self.lineEdit_32.setFont(font2)
        self.lineEdit_32.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_32, 1, 1, 1, 1)

        self.lineEdit_33 = QLineEdit(self.gridLayoutWidget_6)
        self.lineEdit_33.setObjectName(u"lineEdit_33")
        self.lineEdit_33.setMinimumSize(QSize(0, 35))
        self.lineEdit_33.setFont(font2)
        self.lineEdit_33.setStyleSheet(u"")

        self.gridLayout.addWidget(self.lineEdit_33, 0, 1, 1, 1)

        self.label_59 = QLabel(self.gridLayoutWidget_6)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setFont(font3)
        self.label_59.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout.addWidget(self.label_59, 0, 0, 1, 1)

        self.pushButton_34 = QPushButton(self.frame_5)
        self.pushButton_34.setObjectName(u"pushButton_34")
        self.pushButton_34.setGeometry(QRect(1120, 75, 41, 28))
        self.pushButton_34.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon9 = QIcon()
        icon9.addFile(u":/Icon/Recursos/Profile.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_34.setIcon(icon9)
        self.pushButton_34.setIconSize(QSize(30, 23))
        self.pushButton_35 = QPushButton(self.frame_5)
        self.pushButton_35.setObjectName(u"pushButton_35")
        self.pushButton_35.setGeometry(QRect(1120, 125, 41, 28))
        self.pushButton_35.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon10 = QIcon()
        icon10.addFile(u":/Icon/Recursos/IDM.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_35.setIcon(icon10)
        self.pushButton_35.setIconSize(QSize(30, 30))
        self.pushButton_36 = QPushButton(self.frame_5)
        self.pushButton_36.setObjectName(u"pushButton_36")
        self.pushButton_36.setGeometry(QRect(1105, 300, 101, 31))
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
        self.pushButton_36.setPalette(palette)
        font4 = QFont()
        font4.setFamilies([u"Montserrat"])
        font4.setPointSize(8)
        self.pushButton_36.setFont(font4)
        self.pushButton_36.setMouseTracking(False)
        icon11 = QIcon()
        icon11.addFile(u":/Icon/Recursos/Registrar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_36.setIcon(icon11)
        self.pushButton_36.setIconSize(QSize(100, 44))
        self.pushButton_36.setAutoDefault(False)
        self.pushButton_37 = QPushButton(self.frame_5)
        self.pushButton_37.setObjectName(u"pushButton_37")
        self.pushButton_37.setGeometry(QRect(1105, 360, 100, 30))
        font5 = QFont()
        font5.setFamilies([u"Montserrat"])
        self.pushButton_37.setFont(font5)
        self.pushButton_37.setMouseTracking(False)
        icon12 = QIcon()
        icon12.addFile(u":/Icon/Recursos/Modificar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_37.setIcon(icon12)
        self.pushButton_37.setIconSize(QSize(100, 44))
        self.pushButton_37.setAutoDefault(False)
        self.TInstrumentoReparacion = QTableWidget(self.frame_5)
        if (self.TInstrumentoReparacion.columnCount() < 7):
            self.TInstrumentoReparacion.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.TInstrumentoReparacion.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.TInstrumentoReparacion.setObjectName(u"TInstrumentoReparacion")
        self.TInstrumentoReparacion.setGeometry(QRect(30, 260, 1021, 181))
        self.TInstrumentoReparacion.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.TInstrumentoReparacion.horizontalHeader().setDefaultSectionSize(145)
        self.label_72 = QLabel(self.frame_5)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setGeometry(QRect(50, 10, 321, 31))
        font6 = QFont()
        font6.setFamilies([u"Arial"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label_72.setFont(font6)
        self.label_72.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.widget_3 = QWidget(self.tab_5)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 470, 1243, 251))
        self.widget_3.setStyleSheet(u"QWidget{\n"
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
        self.label_60 = QLabel(self.widget_3)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setGeometry(QRect(30, 20, 151, 16))
        font7 = QFont()
        font7.setFamilies([u"Arial"])
        font7.setPointSize(10)
        self.label_60.setFont(font7)
        self.label_60.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.label_61 = QLabel(self.widget_3)
        self.label_61.setObjectName(u"label_61")
        self.label_61.setGeometry(QRect(850, 66, 111, 35))
        self.label_61.setFont(font3)
        self.label_61.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBoxBuscarInstrumentoReparacion = QComboBox(self.widget_3)
        self.comboBoxBuscarInstrumentoReparacion.addItem("")
        self.comboBoxBuscarInstrumentoReparacion.setObjectName(u"comboBoxBuscarInstrumentoReparacion")
        self.comboBoxBuscarInstrumentoReparacion.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBoxBuscarInstrumentoReparacion.setMinimumSize(QSize(181, 35))
        font8 = QFont()
        font8.setFamilies([u"Arial"])
        font8.setStyleStrategy(QFont.PreferDefault)
        self.comboBoxBuscarInstrumentoReparacion.setFont(font8)
        self.comboBoxBuscarInstrumentoReparacion.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 10px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBoxBuscarInstrumentoReparacion.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBoxBuscarInstrumentoReparacion.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBoxBuscarInstrumentoReparacion.setFrame(False)
        self.label_62 = QLabel(self.widget_3)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setGeometry(QRect(850, 136, 45, 35))
        self.label_62.setFont(font3)
        self.label_62.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_34 = QLineEdit(self.widget_3)
        self.lineEdit_34.setObjectName(u"lineEdit_34")
        self.lineEdit_34.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_34.setMinimumSize(QSize(0, 35))
        self.lineEdit_34.setFont(font2)
        self.lineEdit_34.setStyleSheet(u"")
        self.pushButton_39 = QPushButton(self.widget_3)
        self.pushButton_39.setObjectName(u"pushButton_39")
        self.pushButton_39.setGeometry(QRect(1270, 200, 104, 31))
        self.pushButton_39.setMouseTracking(False)
        self.pushButton_39.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon13 = QIcon()
        icon13.addFile(u":/Icon/Componente 29 \u2013 6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_39.setIcon(icon13)
        self.pushButton_39.setIconSize(QSize(100, 31))
        self.pushButton_39.setAutoDefault(False)
        self.pushButton_40 = QPushButton(self.widget_3)
        self.pushButton_40.setObjectName(u"pushButton_40")
        self.pushButton_40.setGeometry(QRect(1440, 200, 104, 31))
        self.pushButton_40.setMouseTracking(False)
        self.pushButton_40.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        icon14 = QIcon()
        icon14.addFile(u":/Icon/Componente 28 \u2013 6.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_40.setIcon(icon14)
        self.pushButton_40.setIconSize(QSize(101, 35))
        self.pushButton_40.setAutoDefault(False)
        self.pushButton_41 = QPushButton(self.widget_3)
        self.pushButton_41.setObjectName(u"pushButton_41")
        self.pushButton_41.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_41.setFont(font5)
        icon15 = QIcon()
        icon15.addFile(u":/Icon/Recursos/Eliminar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_41.setIcon(icon15)
        self.pushButton_42 = QPushButton(self.widget_3)
        self.pushButton_42.setObjectName(u"pushButton_42")
        self.pushButton_42.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_42.setFont(font5)
        icon16 = QIcon()
        icon16.addFile(u":/Icon/Recursos/Consultar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_42.setIcon(icon16)
        self.TConsultaInstrumentoReparacion = QTableWidget(self.widget_3)
        if (self.TConsultaInstrumentoReparacion.columnCount() < 7):
            self.TConsultaInstrumentoReparacion.setColumnCount(7)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(4, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(5, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.TConsultaInstrumentoReparacion.setHorizontalHeaderItem(6, __qtablewidgetitem13)
        self.TConsultaInstrumentoReparacion.setObjectName(u"TConsultaInstrumentoReparacion")
        self.TConsultaInstrumentoReparacion.setGeometry(QRect(20, 50, 810, 180))
        self.TConsultaInstrumentoReparacion.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.tabWidget_3.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.frame_6 = QFrame(self.tab_6)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 1243, 461))
        self.frame_6.setFont(font2)
        self.frame_6.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_6.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_7 = QWidget(self.frame_6)
        self.gridLayoutWidget_7.setObjectName(u"gridLayoutWidget_7")
        self.gridLayoutWidget_7.setGeometry(QRect(50, 50, 381, 191))
        self.gridLayout_7 = QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.label_63 = QLabel(self.gridLayoutWidget_7)
        self.label_63.setObjectName(u"label_63")
        self.label_63.setFont(font3)
        self.label_63.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_7.addWidget(self.label_63, 1, 0, 1, 1)

        self.label_64 = QLabel(self.gridLayoutWidget_7)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font3)
        self.label_64.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_7.addWidget(self.label_64, 2, 0, 1, 1)

        self.dateEdit_7 = QDateEdit(self.gridLayoutWidget_7)
        self.dateEdit_7.setObjectName(u"dateEdit_7")
        self.dateEdit_7.setMinimumSize(QSize(0, 35))
        self.dateEdit_7.setFont(font2)
        self.dateEdit_7.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_7.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_7.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_7.addWidget(self.dateEdit_7, 1, 1, 1, 1)

        self.dateEdit_8 = QDateEdit(self.gridLayoutWidget_7)
        self.dateEdit_8.setObjectName(u"dateEdit_8")
        self.dateEdit_8.setMinimumSize(QSize(0, 35))
        self.dateEdit_8.setFont(font2)
        self.dateEdit_8.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 17px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_8.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_8.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_7.addWidget(self.dateEdit_8, 2, 1, 1, 1)

        self.lineEdit_35 = QLineEdit(self.gridLayoutWidget_7)
        self.lineEdit_35.setObjectName(u"lineEdit_35")
        self.lineEdit_35.setMinimumSize(QSize(0, 35))
        self.lineEdit_35.setFont(font2)
        self.lineEdit_35.setStyleSheet(u"")

        self.gridLayout_7.addWidget(self.lineEdit_35, 0, 1, 1, 1)

        self.label_65 = QLabel(self.gridLayoutWidget_7)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setFont(font3)
        self.label_65.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_7.addWidget(self.label_65, 0, 0, 1, 1)

        self.label_66 = QLabel(self.gridLayoutWidget_7)
        self.label_66.setObjectName(u"label_66")
        self.label_66.setFont(font3)
        self.label_66.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_7.addWidget(self.label_66, 0, 4, 1, 1)

        self.textEdit_2 = QTextEdit(self.frame_6)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setGeometry(QRect(440, 60, 311, 161))
        self.textEdit_2.setStyleSheet(u"QTextEdit{\n"
"background: #FBD27E;\n"
"}")
        self.gridLayoutWidget_8 = QWidget(self.frame_6)
        self.gridLayoutWidget_8.setObjectName(u"gridLayoutWidget_8")
        self.gridLayoutWidget_8.setGeometry(QRect(760, 60, 341, 114))
        self.gridLayout_8 = QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.label_67 = QLabel(self.gridLayoutWidget_8)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font3)
        self.label_67.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_8.addWidget(self.label_67, 1, 0, 1, 1)

        self.lineEdit_36 = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_36.setObjectName(u"lineEdit_36")
        self.lineEdit_36.setMinimumSize(QSize(0, 35))
        self.lineEdit_36.setFont(font2)
        self.lineEdit_36.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_36, 1, 1, 1, 1)

        self.lineEdit_37 = QLineEdit(self.gridLayoutWidget_8)
        self.lineEdit_37.setObjectName(u"lineEdit_37")
        self.lineEdit_37.setMinimumSize(QSize(0, 35))
        self.lineEdit_37.setFont(font2)
        self.lineEdit_37.setStyleSheet(u"")

        self.gridLayout_8.addWidget(self.lineEdit_37, 0, 1, 1, 1)

        self.label_68 = QLabel(self.gridLayoutWidget_8)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setFont(font3)
        self.label_68.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_8.addWidget(self.label_68, 0, 0, 1, 1)

        self.pushButton_43 = QPushButton(self.frame_6)
        self.pushButton_43.setObjectName(u"pushButton_43")
        self.pushButton_43.setGeometry(QRect(1120, 75, 41, 28))
        self.pushButton_43.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_43.setIcon(icon9)
        self.pushButton_43.setIconSize(QSize(30, 23))
        self.pushButton_44 = QPushButton(self.frame_6)
        self.pushButton_44.setObjectName(u"pushButton_44")
        self.pushButton_44.setGeometry(QRect(1120, 125, 41, 28))
        self.pushButton_44.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_44.setIcon(icon10)
        self.pushButton_44.setIconSize(QSize(30, 30))
        self.pushButton_45 = QPushButton(self.frame_6)
        self.pushButton_45.setObjectName(u"pushButton_45")
        self.pushButton_45.setGeometry(QRect(1105, 300, 101, 31))
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
        self.pushButton_45.setPalette(palette1)
        self.pushButton_45.setFont(font4)
        self.pushButton_45.setMouseTracking(False)
        self.pushButton_45.setIcon(icon11)
        self.pushButton_45.setIconSize(QSize(100, 44))
        self.pushButton_45.setAutoDefault(False)
        self.pushButton_46 = QPushButton(self.frame_6)
        self.pushButton_46.setObjectName(u"pushButton_46")
        self.pushButton_46.setGeometry(QRect(1105, 360, 100, 30))
        self.pushButton_46.setFont(font5)
        self.pushButton_46.setMouseTracking(False)
        self.pushButton_46.setIcon(icon12)
        self.pushButton_46.setIconSize(QSize(100, 44))
        self.pushButton_46.setAutoDefault(False)
        self.tableWidget_11 = QTableWidget(self.frame_6)
        self.tableWidget_11.setObjectName(u"tableWidget_11")
        self.tableWidget_11.setGeometry(QRect(30, 260, 1021, 181))
        self.tableWidget_11.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.pushButton_47 = QPushButton(self.frame_6)
        self.pushButton_47.setObjectName(u"pushButton_47")
        self.pushButton_47.setGeometry(QRect(1060, 270, 31, 31))
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
        self.pushButton_47.setPalette(palette2)
        self.pushButton_47.setFont(font4)
        self.pushButton_47.setMouseTracking(False)
        self.pushButton_47.setIconSize(QSize(100, 44))
        self.pushButton_47.setAutoDefault(False)
        self.label_73 = QLabel(self.frame_6)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setGeometry(QRect(50, 10, 321, 31))
        self.label_73.setFont(font6)
        self.label_73.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.widget_8 = QWidget(self.tab_6)
        self.widget_8.setObjectName(u"widget_8")
        self.widget_8.setGeometry(QRect(0, 470, 1243, 251))
        self.widget_8.setStyleSheet(u"QWidget{\n"
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
        self.label_69 = QLabel(self.widget_8)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setGeometry(QRect(30, 20, 151, 16))
        self.label_69.setFont(font7)
        self.label_69.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.pushButton_48 = QPushButton(self.widget_8)
        self.pushButton_48.setObjectName(u"pushButton_48")
        self.pushButton_48.setGeometry(QRect(1290, 210, 101, 31))
        self.pushButton_48.setMouseTracking(False)
        self.pushButton_48.setIcon(icon13)
        self.pushButton_48.setIconSize(QSize(100, 31))
        self.pushButton_48.setAutoDefault(False)
        self.pushButton_49 = QPushButton(self.widget_8)
        self.pushButton_49.setObjectName(u"pushButton_49")
        self.pushButton_49.setGeometry(QRect(1410, 210, 101, 31))
        self.pushButton_49.setMouseTracking(False)
        self.pushButton_49.setIcon(icon14)
        self.pushButton_49.setIconSize(QSize(101, 35))
        self.pushButton_49.setAutoDefault(False)
        self.label_70 = QLabel(self.widget_8)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setGeometry(QRect(850, 70, 115, 28))
        self.label_70.setFont(font3)
        self.label_70.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBox_10 = QComboBox(self.widget_8)
        self.comboBox_10.setObjectName(u"comboBox_10")
        self.comboBox_10.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBox_10.setMinimumSize(QSize(181, 35))
        self.comboBox_10.setFont(font8)
        self.comboBox_10.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 10px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBox_10.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBox_10.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBox_10.setFrame(False)
        self.label_71 = QLabel(self.widget_8)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setGeometry(QRect(850, 140, 45, 28))
        self.label_71.setFont(font3)
        self.label_71.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_38 = QLineEdit(self.widget_8)
        self.lineEdit_38.setObjectName(u"lineEdit_38")
        self.lineEdit_38.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_38.setMinimumSize(QSize(0, 35))
        self.lineEdit_38.setFont(font2)
        self.lineEdit_38.setStyleSheet(u"")
        self.pushButton_50 = QPushButton(self.widget_8)
        self.pushButton_50.setObjectName(u"pushButton_50")
        self.pushButton_50.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_50.setFont(font5)
        self.pushButton_50.setIcon(icon15)
        self.pushButton_51 = QPushButton(self.widget_8)
        self.pushButton_51.setObjectName(u"pushButton_51")
        self.pushButton_51.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_51.setFont(font5)
        self.pushButton_51.setIcon(icon16)
        self.tableWidget_12 = QTableWidget(self.widget_8)
        self.tableWidget_12.setObjectName(u"tableWidget_12")
        self.tableWidget_12.setGeometry(QRect(20, 50, 810, 180))
        self.tableWidget_12.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.tabWidget_3.addTab(self.tab_6, "")
        self.Wproveedores = QWidget(self.WCentral)
        self.Wproveedores.setObjectName(u"Wproveedores")
        self.Wproveedores.setGeometry(QRect(0, 0, 1250, 0))
        self.widget_4 = QWidget(self.Wproveedores)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(2, 0, 1250, 750))
        self.widget_4.setStyleSheet(u"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}")
        self.frame_9 = QFrame(self.widget_4)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 1243, 461))
        self.frame_9.setFont(font5)
        self.frame_9.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_9.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}\n"
"")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_11 = QWidget(self.frame_9)
        self.gridLayoutWidget_11.setObjectName(u"gridLayoutWidget_11")
        self.gridLayoutWidget_11.setGeometry(QRect(50, 50, 1131, 191))
        self.gridLayout_11 = QGridLayout(self.gridLayoutWidget_11)
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.gridLayout_11.setContentsMargins(0, 0, 0, 0)
        self.label_107 = QLabel(self.gridLayoutWidget_11)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font3)
        self.label_107.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_107, 0, 0, 1, 1)

        self.label_106 = QLabel(self.gridLayoutWidget_11)
        self.label_106.setObjectName(u"label_106")
        self.label_106.setFont(font3)
        self.label_106.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_106, 1, 0, 1, 1)

        self.lineEdit_63 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_63.setObjectName(u"lineEdit_63")
        self.lineEdit_63.setMinimumSize(QSize(0, 35))
        self.lineEdit_63.setFont(font2)
        self.lineEdit_63.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_63, 1, 5, 1, 1)

        self.lineEdit_64 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_64.setObjectName(u"lineEdit_64")
        self.lineEdit_64.setMinimumSize(QSize(0, 35))
        self.lineEdit_64.setFont(font2)
        self.lineEdit_64.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_64, 2, 7, 1, 1)

        self.lineEdit_61 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_61.setObjectName(u"lineEdit_61")
        self.lineEdit_61.setMinimumSize(QSize(0, 35))
        self.lineEdit_61.setFont(font2)
        self.lineEdit_61.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_61, 2, 1, 1, 1)

        self.label_104 = QLabel(self.gridLayoutWidget_11)
        self.label_104.setObjectName(u"label_104")
        self.label_104.setFont(font3)
        self.label_104.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_104, 2, 4, 1, 1)

        self.label_105 = QLabel(self.gridLayoutWidget_11)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font3)
        self.label_105.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_105, 2, 0, 1, 1)

        self.label_100 = QLabel(self.gridLayoutWidget_11)
        self.label_100.setObjectName(u"label_100")
        self.label_100.setFont(font3)
        self.label_100.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_100, 0, 4, 1, 1)

        self.FDiligenciamiento_2 = QDateEdit(self.gridLayoutWidget_11)
        self.FDiligenciamiento_2.setObjectName(u"FDiligenciamiento_2")
        self.FDiligenciamiento_2.setMinimumSize(QSize(0, 35))
        self.FDiligenciamiento_2.setFont(font2)
        self.FDiligenciamiento_2.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 8px;\n"
"background:#FBD27E;\n"
"}")
        self.FDiligenciamiento_2.setDateTime(QDateTime(QDate(2021, 10, 12), QTime(0, 0, 0)))
        self.FDiligenciamiento_2.setMaximumDate(QDate(3000, 12, 31))
        self.FDiligenciamiento_2.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_11.addWidget(self.FDiligenciamiento_2, 0, 1, 1, 1)

        self.label_78 = QLabel(self.gridLayoutWidget_11)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font3)
        self.label_78.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_78, 1, 4, 1, 1)

        self.label_101 = QLabel(self.gridLayoutWidget_11)
        self.label_101.setObjectName(u"label_101")
        self.label_101.setFont(font3)
        self.label_101.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_101, 0, 6, 1, 1)

        self.lineEdit_58 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_58.setObjectName(u"lineEdit_58")
        self.lineEdit_58.setMinimumSize(QSize(0, 35))
        self.lineEdit_58.setFont(font2)
        self.lineEdit_58.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_58, 0, 7, 1, 1)

        self.label_102 = QLabel(self.gridLayoutWidget_11)
        self.label_102.setObjectName(u"label_102")
        self.label_102.setFont(font3)
        self.label_102.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_102, 1, 6, 1, 1)

        self.lineEdit_60 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_60.setObjectName(u"lineEdit_60")
        self.lineEdit_60.setMinimumSize(QSize(0, 35))
        self.lineEdit_60.setFont(font2)
        self.lineEdit_60.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_60, 1, 1, 1, 1)

        self.lineEdit_59 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_59.setObjectName(u"lineEdit_59")
        self.lineEdit_59.setMinimumSize(QSize(0, 35))
        self.lineEdit_59.setFont(font2)
        self.lineEdit_59.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_59, 1, 7, 1, 1)

        self.label_103 = QLabel(self.gridLayoutWidget_11)
        self.label_103.setObjectName(u"label_103")
        self.label_103.setFont(font3)
        self.label_103.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_103, 2, 6, 1, 1)

        self.lineEdit_57 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_57.setObjectName(u"lineEdit_57")
        self.lineEdit_57.setMinimumSize(QSize(0, 35))
        self.lineEdit_57.setFont(font2)
        self.lineEdit_57.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_57, 1, 10, 1, 1)

        self.lineEdit_68 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_68.setObjectName(u"lineEdit_68")
        self.lineEdit_68.setMinimumSize(QSize(0, 35))
        self.lineEdit_68.setFont(font2)
        self.lineEdit_68.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_68, 0, 5, 1, 1)

        self.label_113 = QLabel(self.gridLayoutWidget_11)
        self.label_113.setObjectName(u"label_113")
        self.label_113.setFont(font3)
        self.label_113.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_113, 1, 8, 1, 1)

        self.lineEdit_62 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_62.setObjectName(u"lineEdit_62")
        self.lineEdit_62.setMinimumSize(QSize(0, 35))
        self.lineEdit_62.setFont(font2)
        self.lineEdit_62.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_62, 2, 5, 1, 1)

        self.lineEdit_67 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_67.setObjectName(u"lineEdit_67")
        self.lineEdit_67.setMinimumSize(QSize(0, 35))
        self.lineEdit_67.setFont(font2)
        self.lineEdit_67.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_67, 0, 10, 1, 1)

        self.pushButton_23 = QPushButton(self.gridLayoutWidget_11)
        self.pushButton_23.setObjectName(u"pushButton_23")
        self.pushButton_23.setEnabled(True)
        self.pushButton_23.setMaximumSize(QSize(30, 30))
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
        self.pushButton_23.setFont(font4)
        self.pushButton_23.setMouseTracking(False)
        self.pushButton_23.setIcon(icon3)
        self.pushButton_23.setIconSize(QSize(100, 44))
        self.pushButton_23.setAutoDefault(False)

        self.gridLayout_11.addWidget(self.pushButton_23, 2, 8, 1, 1)

        self.label_112 = QLabel(self.gridLayoutWidget_11)
        self.label_112.setObjectName(u"label_112")
        self.label_112.setFont(font3)
        self.label_112.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_11.addWidget(self.label_112, 0, 8, 1, 1)

        self.lineEdit_65 = QLineEdit(self.gridLayoutWidget_11)
        self.lineEdit_65.setObjectName(u"lineEdit_65")
        self.lineEdit_65.setMinimumSize(QSize(0, 35))
        self.lineEdit_65.setFont(font2)
        self.lineEdit_65.setStyleSheet(u"")

        self.gridLayout_11.addWidget(self.lineEdit_65, 2, 10, 1, 1)

        self.pushButton_61 = QPushButton(self.frame_9)
        self.pushButton_61.setObjectName(u"pushButton_61")
        self.pushButton_61.setGeometry(QRect(1105, 360, 100, 30))
        self.pushButton_61.setFont(font5)
        self.pushButton_61.setMouseTracking(False)
        self.pushButton_61.setIcon(icon12)
        self.pushButton_61.setIconSize(QSize(100, 44))
        self.pushButton_61.setAutoDefault(False)
        self.pushButton_62 = QPushButton(self.frame_9)
        self.pushButton_62.setObjectName(u"pushButton_62")
        self.pushButton_62.setGeometry(QRect(1105, 300, 101, 31))
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush)
        palette4.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette4.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette4.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette4.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette4.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette4.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_62.setPalette(palette4)
        self.pushButton_62.setFont(font4)
        self.pushButton_62.setMouseTracking(False)
        self.pushButton_62.setIcon(icon11)
        self.pushButton_62.setIconSize(QSize(100, 44))
        self.pushButton_62.setAutoDefault(False)
        self.label_108 = QLabel(self.frame_9)
        self.label_108.setObjectName(u"label_108")
        self.label_108.setGeometry(QRect(50, 10, 321, 31))
        self.label_108.setFont(font6)
        self.label_108.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.TProveedores = QTableWidget(self.frame_9)
        if (self.TProveedores.columnCount() < 12):
            self.TProveedores.setColumnCount(12)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(7, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(8, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(9, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(10, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.TProveedores.setHorizontalHeaderItem(11, __qtablewidgetitem25)
        self.TProveedores.setObjectName(u"TProveedores")
        self.TProveedores.setGeometry(QRect(30, 260, 1021, 181))
        self.TProveedores.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.TProveedores.setRowCount(0)
        self.TProveedores.setColumnCount(12)
        self.TProveedores.horizontalHeader().setMinimumSectionSize(40)
        self.TProveedores.horizontalHeader().setDefaultSectionSize(120)
        self.TProveedores.verticalHeader().setDefaultSectionSize(30)
        self.widget_11 = QWidget(self.widget_4)
        self.widget_11.setObjectName(u"widget_11")
        self.widget_11.setGeometry(QRect(0, 470, 1243, 251))
        self.widget_11.setStyleSheet(u"QWidget{\n"
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
        self.label_109 = QLabel(self.widget_11)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setGeometry(QRect(30, 20, 151, 16))
        self.label_109.setFont(font7)
        self.label_109.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.label_110 = QLabel(self.widget_11)
        self.label_110.setObjectName(u"label_110")
        self.label_110.setGeometry(QRect(850, 66, 111, 35))
        self.label_110.setFont(font3)
        self.label_110.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBoxBProveedores = QComboBox(self.widget_11)
        self.comboBoxBProveedores.addItem("")
        self.comboBoxBProveedores.setObjectName(u"comboBoxBProveedores")
        self.comboBoxBProveedores.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBoxBProveedores.setMinimumSize(QSize(181, 35))
        self.comboBoxBProveedores.setFont(font8)
        self.comboBoxBProveedores.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 5px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBoxBProveedores.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBoxBProveedores.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBoxBProveedores.setFrame(False)
        self.label_111 = QLabel(self.widget_11)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setGeometry(QRect(850, 136, 45, 35))
        self.label_111.setFont(font3)
        self.label_111.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_66 = QLineEdit(self.widget_11)
        self.lineEdit_66.setObjectName(u"lineEdit_66")
        self.lineEdit_66.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_66.setMinimumSize(QSize(0, 35))
        self.lineEdit_66.setFont(font2)
        self.lineEdit_66.setStyleSheet(u"")
        self.pushButton_63 = QPushButton(self.widget_11)
        self.pushButton_63.setObjectName(u"pushButton_63")
        self.pushButton_63.setGeometry(QRect(1270, 200, 104, 31))
        self.pushButton_63.setMouseTracking(False)
        self.pushButton_63.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_63.setIcon(icon13)
        self.pushButton_63.setIconSize(QSize(100, 31))
        self.pushButton_63.setAutoDefault(False)
        self.pushButton_64 = QPushButton(self.widget_11)
        self.pushButton_64.setObjectName(u"pushButton_64")
        self.pushButton_64.setGeometry(QRect(1440, 200, 104, 31))
        self.pushButton_64.setMouseTracking(False)
        self.pushButton_64.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_64.setIcon(icon14)
        self.pushButton_64.setIconSize(QSize(101, 35))
        self.pushButton_64.setAutoDefault(False)
        self.pushButton_65 = QPushButton(self.widget_11)
        self.pushButton_65.setObjectName(u"pushButton_65")
        self.pushButton_65.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_65.setFont(font5)
        self.pushButton_65.setIcon(icon15)
        self.pushButton_66 = QPushButton(self.widget_11)
        self.pushButton_66.setObjectName(u"pushButton_66")
        self.pushButton_66.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_66.setFont(font5)
        self.pushButton_66.setIcon(icon16)
        self.TConsultaProveedores = QTableWidget(self.widget_11)
        if (self.TConsultaProveedores.columnCount() < 11):
            self.TConsultaProveedores.setColumnCount(11)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(0, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(1, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(2, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(3, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(4, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(5, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(6, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(7, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(8, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(9, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.TConsultaProveedores.setHorizontalHeaderItem(10, __qtablewidgetitem36)
        self.TConsultaProveedores.setObjectName(u"TConsultaProveedores")
        self.TConsultaProveedores.setGeometry(QRect(20, 50, 810, 180))
        self.TConsultaProveedores.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.Wregistrar = QWidget(self.WCentral)
        self.Wregistrar.setObjectName(u"Wregistrar")
        self.Wregistrar.setGeometry(QRect(0, 0, 1250, 750))
        self.Wregistrar.setStyleSheet(u"QPushButton{\n"
"Background-color:rgb(255, 255, 255);\n"
"border: 1px solid #003057;\n"
"border-radius: 6px;\n"
"}")
        self.frame_7 = QFrame(self.Wregistrar)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(0, 0, 1243, 461))
        self.frame_7.setFont(font5)
        self.frame_7.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.frame_7.setStyleSheet(u"QFrame{\n"
"border: 2px solid;\n"
"border-radius: 25px;\n"
"background: #ffffff;\n"
"}\n"
"QLineEdit{\n"
"Border: 2px solid black;\n"
"border-radius: 17px;\n"
"Background: #FBD27E;\n"
"}\n"
"")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.gridLayoutWidget_9 = QWidget(self.frame_7)
        self.gridLayoutWidget_9.setObjectName(u"gridLayoutWidget_9")
        self.gridLayoutWidget_9.setGeometry(QRect(50, 50, 1001, 191))
        self.gridLayout_9 = QGridLayout(self.gridLayoutWidget_9)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.lineEdit_39 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_39.setObjectName(u"lineEdit_39")
        self.lineEdit_39.setMinimumSize(QSize(0, 35))
        self.lineEdit_39.setFont(font2)
        self.lineEdit_39.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_39, 0, 1, 1, 1)

        self.label_74 = QLabel(self.gridLayoutWidget_9)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setFont(font3)
        self.label_74.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_74, 0, 0, 1, 1)

        self.label_75 = QLabel(self.gridLayoutWidget_9)
        self.label_75.setObjectName(u"label_75")
        self.label_75.setFont(font3)
        self.label_75.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_75, 1, 4, 1, 1)

        self.lineEdit_40 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_40.setObjectName(u"lineEdit_40")
        self.lineEdit_40.setMinimumSize(QSize(0, 35))
        self.lineEdit_40.setFont(font2)
        self.lineEdit_40.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_40, 0, 5, 1, 1)

        self.label_76 = QLabel(self.gridLayoutWidget_9)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font3)
        self.label_76.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_76, 0, 4, 1, 1)

        self.lineEdit_41 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_41.setObjectName(u"lineEdit_41")
        self.lineEdit_41.setMinimumSize(QSize(0, 35))
        self.lineEdit_41.setFont(font2)
        self.lineEdit_41.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_41, 0, 7, 1, 1)

        self.label_77 = QLabel(self.gridLayoutWidget_9)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setFont(font3)
        self.label_77.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_77, 0, 6, 1, 1)

        self.lineEdit_42 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_42.setObjectName(u"lineEdit_42")
        self.lineEdit_42.setMinimumSize(QSize(0, 35))
        self.lineEdit_42.setFont(font2)
        self.lineEdit_42.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_42, 1, 7, 1, 1)

        self.lineEdit_43 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_43.setObjectName(u"lineEdit_43")
        self.lineEdit_43.setMinimumSize(QSize(0, 35))
        self.lineEdit_43.setFont(font2)
        self.lineEdit_43.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_43, 1, 1, 1, 1)

        self.label_79 = QLabel(self.gridLayoutWidget_9)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font3)
        self.label_79.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_79, 1, 0, 1, 1)

        self.label_80 = QLabel(self.gridLayoutWidget_9)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font3)
        self.label_80.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_80, 1, 6, 1, 1)

        self.label_81 = QLabel(self.gridLayoutWidget_9)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font3)
        self.label_81.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_81, 2, 6, 1, 1)

        self.dateEdit_9 = QDateEdit(self.gridLayoutWidget_9)
        self.dateEdit_9.setObjectName(u"dateEdit_9")
        self.dateEdit_9.setMinimumSize(QSize(0, 35))
        self.dateEdit_9.setFont(font2)
        self.dateEdit_9.setStyleSheet(u"QDateEdit{\n"
"Border: 2px solid black;\n"
"Border-radius: 8px;\n"
"background:#FBD27E;\n"
"}")
        self.dateEdit_9.setDateTime(QDateTime(QDate(2021, 10, 12), QTime(0, 0, 0)))
        self.dateEdit_9.setMaximumDate(QDate(3000, 12, 31))
        self.dateEdit_9.setMinimumDate(QDate(2021, 5, 17))

        self.gridLayout_9.addWidget(self.dateEdit_9, 2, 7, 1, 1)

        self.label_82 = QLabel(self.gridLayoutWidget_9)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setFont(font3)
        self.label_82.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_82, 2, 0, 1, 1)

        self.label_83 = QLabel(self.gridLayoutWidget_9)
        self.label_83.setObjectName(u"label_83")
        self.label_83.setFont(font3)
        self.label_83.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")

        self.gridLayout_9.addWidget(self.label_83, 2, 4, 1, 1)

        self.lineEdit_44 = QLineEdit(self.gridLayoutWidget_9)
        self.lineEdit_44.setObjectName(u"lineEdit_44")
        self.lineEdit_44.setMinimumSize(QSize(0, 35))
        self.lineEdit_44.setFont(font2)
        self.lineEdit_44.setStyleSheet(u"")

        self.gridLayout_9.addWidget(self.lineEdit_44, 2, 5, 1, 1)

        self.comboBoxEstadoEquipo = QComboBox(self.gridLayoutWidget_9)
        self.comboBoxEstadoEquipo.setObjectName(u"comboBoxEstadoEquipo")
        self.comboBoxEstadoEquipo.setMinimumSize(QSize(0, 35))
        self.comboBoxEstadoEquipo.setFont(font8)
        self.comboBoxEstadoEquipo.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 8px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBoxEstadoEquipo.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBoxEstadoEquipo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBoxEstadoEquipo.setFrame(False)

        self.gridLayout_9.addWidget(self.comboBoxEstadoEquipo, 1, 5, 1, 1)

        self.comboBoxMantenimientoEquipo = QComboBox(self.gridLayoutWidget_9)
        self.comboBoxMantenimientoEquipo.setObjectName(u"comboBoxMantenimientoEquipo")
        self.comboBoxMantenimientoEquipo.setMinimumSize(QSize(0, 35))
        self.comboBoxMantenimientoEquipo.setFont(font8)
        self.comboBoxMantenimientoEquipo.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 8px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBoxMantenimientoEquipo.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBoxMantenimientoEquipo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBoxMantenimientoEquipo.setFrame(False)

        self.gridLayout_9.addWidget(self.comboBoxMantenimientoEquipo, 2, 1, 1, 1)

        self.pushButton_20 = QPushButton(self.frame_7)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setGeometry(QRect(1105, 360, 100, 30))
        self.pushButton_20.setFont(font5)
        self.pushButton_20.setMouseTracking(False)
        self.pushButton_20.setIcon(icon12)
        self.pushButton_20.setIconSize(QSize(100, 44))
        self.pushButton_20.setAutoDefault(False)
        self.pushButton_21 = QPushButton(self.frame_7)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setGeometry(QRect(1105, 300, 101, 31))
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Active, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Active, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Active, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Active, QPalette.Text, brush)
        palette5.setBrush(QPalette.Active, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Active, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Active, QPalette.AlternateBase, brush4)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Inactive, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Inactive, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Inactive, QPalette.Text, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.ButtonText, brush)
        palette5.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush4)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette5.setBrush(QPalette.Disabled, QPalette.Midlight, brush3)
        palette5.setBrush(QPalette.Disabled, QPalette.Dark, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Mid, brush5)
        palette5.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.BrightText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        palette5.setBrush(QPalette.Disabled, QPalette.Base, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Window, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette5.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush7)
        palette5.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
        self.pushButton_21.setPalette(palette5)
        self.pushButton_21.setFont(font4)
        self.pushButton_21.setMouseTracking(False)
        self.pushButton_21.setIcon(icon11)
        self.pushButton_21.setIconSize(QSize(100, 44))
        self.pushButton_21.setAutoDefault(False)
        self.label_84 = QLabel(self.frame_7)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setGeometry(QRect(50, 10, 321, 31))
        self.label_84.setFont(font6)
        self.label_84.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.Tequipos = QTableWidget(self.frame_7)
        if (self.Tequipos.columnCount() < 9):
            self.Tequipos.setColumnCount(9)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(3, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(4, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(5, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(6, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(7, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.Tequipos.setHorizontalHeaderItem(8, __qtablewidgetitem45)
        self.Tequipos.setObjectName(u"Tequipos")
        self.Tequipos.setGeometry(QRect(30, 260, 1021, 181))
        self.Tequipos.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")
        self.Tequipos.setRowCount(0)
        self.Tequipos.setColumnCount(9)
        self.Tequipos.horizontalHeader().setMinimumSectionSize(40)
        self.Tequipos.horizontalHeader().setDefaultSectionSize(120)
        self.Tequipos.verticalHeader().setDefaultSectionSize(30)
        self.widget_9 = QWidget(self.Wregistrar)
        self.widget_9.setObjectName(u"widget_9")
        self.widget_9.setGeometry(QRect(0, 470, 1243, 251))
        self.widget_9.setStyleSheet(u"QWidget{\n"
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
        self.label_85 = QLabel(self.widget_9)
        self.label_85.setObjectName(u"label_85")
        self.label_85.setGeometry(QRect(30, 20, 151, 16))
        self.label_85.setFont(font7)
        self.label_85.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.label_86 = QLabel(self.widget_9)
        self.label_86.setObjectName(u"label_86")
        self.label_86.setGeometry(QRect(850, 66, 111, 35))
        self.label_86.setFont(font3)
        self.label_86.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.comboBoxBuscarEquipo = QComboBox(self.widget_9)
        self.comboBoxBuscarEquipo.addItem("")
        self.comboBoxBuscarEquipo.setObjectName(u"comboBoxBuscarEquipo")
        self.comboBoxBuscarEquipo.setGeometry(QRect(1030, 70, 181, 35))
        self.comboBoxBuscarEquipo.setMinimumSize(QSize(181, 35))
        self.comboBoxBuscarEquipo.setFont(font8)
        self.comboBoxBuscarEquipo.setStyleSheet(u"QComboBox{\n"
"Border: 2px solid black;\n"
"Border-radius: 5px;\n"
"background:#FBD27E;\n"
"}")
        self.comboBoxBuscarEquipo.setInsertPolicy(QComboBox.InsertAtBottom)
        self.comboBoxBuscarEquipo.setSizeAdjustPolicy(QComboBox.AdjustToContents)
        self.comboBoxBuscarEquipo.setFrame(False)
        self.label_87 = QLabel(self.widget_9)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setGeometry(QRect(850, 136, 45, 35))
        self.label_87.setFont(font3)
        self.label_87.setStyleSheet(u"QLabel{\n"
"border: white;\n"
"}")
        self.lineEdit_46 = QLineEdit(self.widget_9)
        self.lineEdit_46.setObjectName(u"lineEdit_46")
        self.lineEdit_46.setGeometry(QRect(1030, 140, 181, 35))
        self.lineEdit_46.setMinimumSize(QSize(0, 35))
        self.lineEdit_46.setFont(font2)
        self.lineEdit_46.setStyleSheet(u"")
        self.pushButton_38 = QPushButton(self.widget_9)
        self.pushButton_38.setObjectName(u"pushButton_38")
        self.pushButton_38.setGeometry(QRect(1270, 200, 104, 31))
        self.pushButton_38.setMouseTracking(False)
        self.pushButton_38.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_38.setIcon(icon13)
        self.pushButton_38.setIconSize(QSize(100, 31))
        self.pushButton_38.setAutoDefault(False)
        self.pushButton_52 = QPushButton(self.widget_9)
        self.pushButton_52.setObjectName(u"pushButton_52")
        self.pushButton_52.setGeometry(QRect(1440, 200, 104, 31))
        self.pushButton_52.setMouseTracking(False)
        self.pushButton_52.setStyleSheet(u"QPushButton{\n"
"background: #ffffff;\n"
"}")
        self.pushButton_52.setIcon(icon14)
        self.pushButton_52.setIconSize(QSize(101, 35))
        self.pushButton_52.setAutoDefault(False)
        self.pushButton_53 = QPushButton(self.widget_9)
        self.pushButton_53.setObjectName(u"pushButton_53")
        self.pushButton_53.setGeometry(QRect(900, 200, 93, 28))
        self.pushButton_53.setFont(font5)
        self.pushButton_53.setIcon(icon15)
        self.pushButton_54 = QPushButton(self.widget_9)
        self.pushButton_54.setObjectName(u"pushButton_54")
        self.pushButton_54.setGeometry(QRect(1060, 200, 93, 28))
        self.pushButton_54.setFont(font5)
        self.pushButton_54.setIcon(icon16)
        self.TConsultaInstrumento = QTableWidget(self.widget_9)
        if (self.TConsultaInstrumento.columnCount() < 9):
            self.TConsultaInstrumento.setColumnCount(9)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(0, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(1, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(2, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(3, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(4, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(5, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(6, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(7, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        self.TConsultaInstrumento.setHorizontalHeaderItem(8, __qtablewidgetitem54)
        self.TConsultaInstrumento.setObjectName(u"TConsultaInstrumento")
        self.TConsultaInstrumento.setGeometry(QRect(20, 50, 810, 180))
        self.TConsultaInstrumento.setStyleSheet(u"QTableWidget{\n"
"border-radius: 8px \n"
"}")

        self.verticalLayout.addWidget(self.widget_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget_3.setCurrentIndex(0)
        self.pushButton_36.setDefault(False)
        self.pushButton_37.setDefault(False)
        self.pushButton_39.setDefault(False)
        self.pushButton_40.setDefault(False)
        self.pushButton_45.setDefault(False)
        self.pushButton_46.setDefault(False)
        self.pushButton_47.setDefault(False)
        self.pushButton_48.setDefault(False)
        self.pushButton_49.setDefault(False)
        self.pushButton_23.setDefault(False)
        self.pushButton_61.setDefault(False)
        self.pushButton_62.setDefault(False)
        self.pushButton_63.setDefault(False)
        self.pushButton_64.setDefault(False)
        self.pushButton_20.setDefault(False)
        self.pushButton_21.setDefault(False)
        self.pushButton_38.setDefault(False)
        self.pushButton_52.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Probando", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"LABORATORISTA", None))
        self.label_3.setText("")
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"     Inicio                                ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"      Registrar                        ", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"     Reparaciones                 ", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"    Mantenimiento M\u00e1quina", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"    Proveedores                       ", None))
        self.pushButton_6.setText(QCoreApplication.translate("MainWindow", u"Asignaci\u00f3n Modelamientos", None))
        self.pushButton_7.setText(QCoreApplication.translate("MainWindow", u"    Consulta Horarios           ", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"    Ayuda                                ", None))
        self.pushButton_9.setText(QCoreApplication.translate("MainWindow", u"   Setting                              ", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Fecha De Ingreso:", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Fecha De Retorno:", None))
        self.dateEdit_5.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/d", None))
        self.dateEdit_6.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/d", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Descripci\u00f3n:", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"ID Instrumento", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"ID Laboratorista", None))
        self.pushButton_34.setText("")
        self.pushButton_35.setText("")
        self.pushButton_36.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.pushButton_37.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        ___qtablewidgetitem = self.TInstrumentoReparacion.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem1 = self.TInstrumentoReparacion.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Fecha Ingreso", None));
        ___qtablewidgetitem2 = self.TInstrumentoReparacion.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Fecha Retorno", None));
        ___qtablewidgetitem3 = self.TInstrumentoReparacion.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem4 = self.TInstrumentoReparacion.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"ID Labaratorista", None));
        ___qtablewidgetitem5 = self.TInstrumentoReparacion.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"ID Maquina", None));
        ___qtablewidgetitem6 = self.TInstrumentoReparacion.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"ID Instrumento", None));
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Reparacion De Instrumentos", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"TABLA CONSULTA", None))
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Filtro De Busqueda", None))
        self.comboBoxBuscarInstrumentoReparacion.setItemText(0, "")

        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.pushButton_39.setText("")
        self.pushButton_40.setText("")
        self.pushButton_41.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_42.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem7 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(0)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem8 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(1)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Fecha Ingreso", None));
        ___qtablewidgetitem9 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(2)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Fecha Retorno", None));
        ___qtablewidgetitem10 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(3)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Descripcion", None));
        ___qtablewidgetitem11 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(4)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Nueva columna", None));
        ___qtablewidgetitem12 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(5)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"ID Maquina", None));
        ___qtablewidgetitem13 = self.TConsultaInstrumentoReparacion.horizontalHeaderItem(6)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"ID Instrumento", None));
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Instrumetos", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Fecha De Ingreso:", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Fecha De Retorno:", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Descripcion:", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"ID M\u00e1quina:", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"ID Laboratorista:", None))
        self.pushButton_43.setText("")
        self.pushButton_44.setText("")
        self.pushButton_45.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.pushButton_46.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.pushButton_47.setText("")
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Reparacion De M\u00e1quinas", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"TABLA CONSULTA", None))
        self.pushButton_48.setText("")
        self.pushButton_49.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Filtro De Busqueda:", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.pushButton_50.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_51.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        self.tabWidget_3.setTabText(self.tabWidget_3.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"M\u00e1quinas", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Fecha De Diligenciamiento:", None))
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Nombre o Razon Social:", None))
        self.lineEdit_61.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Fax:", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Telefonos:", None))
        self.label_100.setText(QCoreApplication.translate("MainWindow", u"NIT:", None))
        self.FDiligenciamiento_2.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/d", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"Direccion:", None))
        self.label_101.setText(QCoreApplication.translate("MainWindow", u"Ciudad:", None))
        self.label_102.setText(QCoreApplication.translate("MainWindow", u"Contacto Ventas:", None))
        self.lineEdit_60.setText("")
        self.label_103.setText(QCoreApplication.translate("MainWindow", u"Contacto Soporte Tecnico:", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"E-mail:", None))
        self.pushButton_23.setText("")
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.pushButton_61.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.pushButton_62.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Registro Proveedores", None))
        ___qtablewidgetitem14 = self.TProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem15 = self.TProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem16 = self.TProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Razon Social", None));
        ___qtablewidgetitem17 = self.TProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"NIT", None));
        ___qtablewidgetitem18 = self.TProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Telefonos", None));
        ___qtablewidgetitem19 = self.TProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem20 = self.TProveedores.horizontalHeaderItem(6)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        ___qtablewidgetitem21 = self.TProveedores.horizontalHeaderItem(7)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Fax", None));
        ___qtablewidgetitem22 = self.TProveedores.horizontalHeaderItem(8)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Ciudad", None));
        ___qtablewidgetitem23 = self.TProveedores.horizontalHeaderItem(9)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Contacto Ventas", None));
        ___qtablewidgetitem24 = self.TProveedores.horizontalHeaderItem(10)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Contacto Soporte Tecnico", None));
        ___qtablewidgetitem25 = self.TProveedores.horizontalHeaderItem(11)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"PDF", None));
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"TABLA CONSULTA", None))
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Filtro De Busqueda", None))
        self.comboBoxBProveedores.setItemText(0, "")

        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.pushButton_63.setText("")
        self.pushButton_64.setText("")
        self.pushButton_65.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_66.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem26 = self.TConsultaProveedores.horizontalHeaderItem(0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem27 = self.TConsultaProveedores.horizontalHeaderItem(1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem28 = self.TConsultaProveedores.horizontalHeaderItem(2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Razon Social", None));
        ___qtablewidgetitem29 = self.TConsultaProveedores.horizontalHeaderItem(3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"NIT", None));
        ___qtablewidgetitem30 = self.TConsultaProveedores.horizontalHeaderItem(4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Telefonos", None));
        ___qtablewidgetitem31 = self.TConsultaProveedores.horizontalHeaderItem(5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"E-mail", None));
        ___qtablewidgetitem32 = self.TConsultaProveedores.horizontalHeaderItem(6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Direccion", None));
        ___qtablewidgetitem33 = self.TConsultaProveedores.horizontalHeaderItem(7)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Fax", None));
        ___qtablewidgetitem34 = self.TConsultaProveedores.horizontalHeaderItem(8)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Ciudad", None));
        ___qtablewidgetitem35 = self.TConsultaProveedores.horizontalHeaderItem(9)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Contacto Ventas", None));
        ___qtablewidgetitem36 = self.TConsultaProveedores.horizontalHeaderItem(10)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Contacto Soporte Tecnico", None));
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"ID:", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Nombre:", None))
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"C\u00f3digo(Placa):", None))
        self.lineEdit_43.setText(QCoreApplication.translate("MainWindow", u"Vida \u00fatil del equipo (En A\u00f1os)", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Vida:", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Fabricante:", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Fecha De Registro:", None))
        self.dateEdit_9.setDisplayFormat(QCoreApplication.translate("MainWindow", u"yyyy/MM/d", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Mantenimiento: ", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Valor:", None))
        self.pushButton_20.setText(QCoreApplication.translate("MainWindow", u"Modificar", None))
        self.pushButton_21.setText(QCoreApplication.translate("MainWindow", u"Registrar", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Registro Equipos", None))
        ___qtablewidgetitem37 = self.Tequipos.horizontalHeaderItem(0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem38 = self.Tequipos.horizontalHeaderItem(1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem39 = self.Tequipos.horizontalHeaderItem(2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Vida \u00fatil", None));
        ___qtablewidgetitem40 = self.Tequipos.horizontalHeaderItem(3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Mantenimientos", None));
        ___qtablewidgetitem41 = self.Tequipos.horizontalHeaderItem(4)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem42 = self.Tequipos.horizontalHeaderItem(5)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem43 = self.Tequipos.horizontalHeaderItem(6)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Fecha Registro", None));
        ___qtablewidgetitem44 = self.Tequipos.horizontalHeaderItem(7)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem45 = self.Tequipos.horizontalHeaderItem(8)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"TABLA CONSULTA", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Filtro De Busqueda", None))
        self.comboBoxBuscarEquipo.setItemText(0, "")

        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Buscar:", None))
        self.pushButton_38.setText("")
        self.pushButton_52.setText("")
        self.pushButton_53.setText(QCoreApplication.translate("MainWindow", u"Eliminar", None))
        self.pushButton_54.setText(QCoreApplication.translate("MainWindow", u"Consultar", None))
        ___qtablewidgetitem46 = self.TConsultaInstrumento.horizontalHeaderItem(0)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem47 = self.TConsultaInstrumento.horizontalHeaderItem(1)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Nombre", None));
        ___qtablewidgetitem48 = self.TConsultaInstrumento.horizontalHeaderItem(2)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Vida \u00fatil", None));
        ___qtablewidgetitem49 = self.TConsultaInstrumento.horizontalHeaderItem(3)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Mantenimientos", None));
        ___qtablewidgetitem50 = self.TConsultaInstrumento.horizontalHeaderItem(4)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"Estado", None));
        ___qtablewidgetitem51 = self.TConsultaInstrumento.horizontalHeaderItem(5)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem52 = self.TConsultaInstrumento.horizontalHeaderItem(6)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Fecha Registro", None));
        ___qtablewidgetitem53 = self.TConsultaInstrumento.horizontalHeaderItem(7)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Fabricante", None));
        ___qtablewidgetitem54 = self.TConsultaInstrumento.horizontalHeaderItem(8)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
    # retranslateUi

