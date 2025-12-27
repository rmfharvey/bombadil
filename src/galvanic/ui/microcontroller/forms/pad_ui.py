# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pad.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QHBoxLayout, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(805, 44)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pad_name_label = QLabel(Form)
        self.pad_name_label.setObjectName(u"pad_name_label")
        self.pad_name_label.setMinimumSize(QSize(80, 0))
        self.pad_name_label.setMaximumSize(QSize(80, 16777215))
        self.pad_name_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.pad_name_label)

        self.function_combobox = QComboBox(Form)
        self.function_combobox.setObjectName(u"function_combobox")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.function_combobox.sizePolicy().hasHeightForWidth())
        self.function_combobox.setSizePolicy(sizePolicy)
        self.function_combobox.setMinimumSize(QSize(150, 0))
        self.function_combobox.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout.addWidget(self.function_combobox)

        self.net_name_lineedit = QLineEdit(Form)
        self.net_name_lineedit.setObjectName(u"net_name_lineedit")
        sizePolicy.setHeightForWidth(self.net_name_lineedit.sizePolicy().hasHeightForWidth())
        self.net_name_lineedit.setSizePolicy(sizePolicy)
        self.net_name_lineedit.setMinimumSize(QSize(250, 0))
        self.net_name_lineedit.setMaximumSize(QSize(250, 16777215))
        self.net_name_lineedit.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.net_name_lineedit)

        self.horizontalSpacer = QSpacerItem(205, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.comment_pushbutton = QPushButton(Form)
        self.comment_pushbutton.setObjectName(u"comment_pushbutton")

        self.horizontalLayout.addWidget(self.comment_pushbutton)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.pad_name_label.setText(QCoreApplication.translate("Form", u"{pad | pin}", None))
        self.net_name_lineedit.setPlaceholderText(QCoreApplication.translate("Form", u"Net Name", None))
        self.comment_pushbutton.setText(QCoreApplication.translate("Form", u"Comment", None))
    # retranslateUi

