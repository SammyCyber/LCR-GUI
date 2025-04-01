# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_2.addWidget(self.label_3)

        self.cb_ports = QComboBox(self.centralwidget)
        self.cb_ports.setObjectName(u"cb_ports")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cb_ports.sizePolicy().hasHeightForWidth())
        self.cb_ports.setSizePolicy(sizePolicy)

        self.horizontalLayout_2.addWidget(self.cb_ports)

        self.btn_rescan = QPushButton(self.centralwidget)
        self.btn_rescan.setObjectName(u"btn_rescan")

        self.horizontalLayout_2.addWidget(self.btn_rescan)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.tb_send_data = QLineEdit(self.centralwidget)
        self.tb_send_data.setObjectName(u"tb_send_data")

        self.horizontalLayout.addWidget(self.tb_send_data)

        self.btn_send_data = QPushButton(self.centralwidget)
        self.btn_send_data.setObjectName(u"btn_send_data")

        self.horizontalLayout.addWidget(self.btn_send_data)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.tb_received_data = QPlainTextEdit(self.centralwidget)
        self.tb_received_data.setObjectName(u"tb_received_data")
        self.tb_received_data.setReadOnly(True)

        self.verticalLayout.addWidget(self.tb_received_data)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 800, 24))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.btn_send_data.clicked.connect(MainWindow.send_data)
        self.btn_rescan.clicked.connect(MainWindow.rescan)
        self.cb_ports.currentTextChanged.connect(MainWindow.connect_to_port)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Connect to:", None))
        self.btn_rescan.setText(QCoreApplication.translate("MainWindow", u"Rescan", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Send data:", None))
        self.btn_send_data.setText(QCoreApplication.translate("MainWindow", u"Send", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Received data:", None))
    # retranslateUi

