# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(433, 107)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 10, 5, 5)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.register_id_label = QLabel(Form)
        self.register_id_label.setObjectName(u"register_id_label")

        self.horizontalLayout.addWidget(self.register_id_label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.frame_data_label = QLabel(Form)
        self.frame_data_label.setObjectName(u"frame_data_label")

        self.horizontalLayout.addWidget(self.frame_data_label)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.register_groupbox = QFrame(Form)
        self.register_groupbox.setObjectName(u"register_groupbox")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.register_groupbox.sizePolicy().hasHeightForWidth())
        self.register_groupbox.setSizePolicy(sizePolicy1)
        self.register_groupbox.setMinimumSize(QSize(0, 60))
        self.register_groupbox.setMaximumSize(QSize(16777215, 100))
        self.register_layout = QHBoxLayout(self.register_groupbox)
        self.register_layout.setSpacing(1)
        self.register_layout.setObjectName(u"register_layout")
        self.register_layout.setContentsMargins(2, 2, 2, 2)

        self.verticalLayout.addWidget(self.register_groupbox)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.register_id_label.setText(QCoreApplication.translate("Form", u"{register_id}", None))
        self.frame_data_label.setText(QCoreApplication.translate("Form", u"{frame_data}", None))
    # retranslateUi

