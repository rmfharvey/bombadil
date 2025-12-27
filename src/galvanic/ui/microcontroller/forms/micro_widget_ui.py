# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'micro_widget.ui'
##
## Created by: Qt User Interface Compiler version 6.9.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QGroupBox, QHBoxLayout,
    QPushButton, QScrollArea, QSizePolicy, QSpacerItem,
    QTabWidget, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1059, 670)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info_groupbox = QGroupBox(Form)
        self.info_groupbox.setObjectName(u"info_groupbox")
        self.info_groupbox.setMinimumSize(QSize(320, 100))
        self.info_groupbox.setMaximumSize(QSize(320, 100))
        self.info_groupbox.setAutoFillBackground(False)
        self.info_groupbox.setAlignment(Qt.AlignCenter)
        self.groupBox_2 = QGroupBox(self.info_groupbox)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(70, 630, 120, 80))

        self.verticalLayout.addWidget(self.info_groupbox)

        self.unassigned_nets_groupbox = QGroupBox(Form)
        self.unassigned_nets_groupbox.setObjectName(u"unassigned_nets_groupbox")
        self.unassigned_nets_groupbox.setMinimumSize(QSize(320, 0))
        self.unassigned_nets_groupbox.setMaximumSize(QSize(320, 16777215))
        self.unassigned_nets_groupbox.setAlignment(Qt.AlignCenter)
        self.unassigned_nets_groupbox.setFlat(False)
        self.verticalLayout_4 = QVBoxLayout(self.unassigned_nets_groupbox)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.unassigned_nets_groupbox)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_4.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.unassigned_nets_groupbox)
        self.pushButton_3.setObjectName(u"pushButton_3")

        self.horizontalLayout_4.addWidget(self.pushButton_3)


        self.verticalLayout_3.addLayout(self.horizontalLayout_4)

        self.pushButton = QPushButton(self.unassigned_nets_groupbox)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout_3.addWidget(self.pushButton)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)

        self.scrollArea = QScrollArea(self.unassigned_nets_groupbox)
        self.scrollArea.setObjectName(u"scrollArea")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.scrollArea.sizePolicy().hasHeightForWidth())
        self.scrollArea.setSizePolicy(sizePolicy)
        self.scrollArea.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 294, 434))
        self.verticalLayout_5 = QVBoxLayout(self.scrollAreaWidgetContents_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalSpacer_2 = QSpacerItem(20, 413, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer_2)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_3)

        self.verticalLayout_4.addWidget(self.scrollArea)


        self.verticalLayout.addWidget(self.unassigned_nets_groupbox)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.io_tabwidget = QTabWidget(Form)
        self.io_tabwidget.setObjectName(u"io_tabwidget")
        self.pad_tab = QWidget()
        self.pad_tab.setObjectName(u"pad_tab")
        self.verticalLayout_2 = QVBoxLayout(self.pad_tab)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pads_frame = QFrame(self.pad_tab)
        self.pads_frame.setObjectName(u"pads_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pads_frame.sizePolicy().hasHeightForWidth())
        self.pads_frame.setSizePolicy(sizePolicy1)
        self.pads_frame.setFrameShape(QFrame.StyledPanel)
        self.pads_frame.setFrameShadow(QFrame.Raised)
        self.pads_frame_layout = QHBoxLayout(self.pads_frame)
        self.pads_frame_layout.setSpacing(1)
        self.pads_frame_layout.setObjectName(u"pads_frame_layout")
        self.pads_frame_layout.setContentsMargins(0, 0, 0, 0)

        self.verticalLayout_2.addWidget(self.pads_frame)

        self.io_tabwidget.addTab(self.pad_tab, "")
        self.io_tab = QWidget()
        self.io_tab.setObjectName(u"io_tab")
        self.io_tabwidget.addTab(self.io_tab, "")

        self.horizontalLayout.addWidget(self.io_tabwidget)


        self.retranslateUi(Form)

        self.io_tabwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.info_groupbox.setTitle(QCoreApplication.translate("Form", u"Micro Info", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"GroupBox", None))
        self.unassigned_nets_groupbox.setTitle(QCoreApplication.translate("Form", u"Unassigned Nets", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"Paste Nets", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"Clear Nets", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"Clear and Paste", None))
        self.io_tabwidget.setTabText(self.io_tabwidget.indexOf(self.pad_tab), QCoreApplication.translate("Form", u"Pads", None))
        self.io_tabwidget.setTabText(self.io_tabwidget.indexOf(self.io_tab), QCoreApplication.translate("Form", u"IO", None))
    # retranslateUi

