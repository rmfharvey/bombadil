# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'field.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QSizePolicy, QVBoxLayout,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(242, 60)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.field_name_label = QLabel(self.frame)
        self.field_name_label.setObjectName(u"field_name_label")
        font = QFont()
        font.setPointSize(11)
        self.field_name_label.setFont(font)
        self.field_name_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout.addWidget(self.field_name_label)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.value_lineedit = QLineEdit(self.frame)
        self.value_lineedit.setObjectName(u"value_lineedit")
        self.value_lineedit.setMinimumSize(QSize(100, 0))
        self.value_lineedit.setMaximumSize(QSize(100, 16777215))

        self.horizontalLayout_2.addWidget(self.value_lineedit)

        self.value_combobox = QComboBox(self.frame)
        self.value_combobox.setObjectName(u"value_combobox")
        self.value_combobox.setMinimumSize(QSize(120, 0))
        self.value_combobox.setMaximumSize(QSize(120, 16777215))
        font1 = QFont()
        font1.setPointSize(10)
        self.value_combobox.setFont(font1)

        self.horizontalLayout_2.addWidget(self.value_combobox)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.horizontalLayout.addWidget(self.frame)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.field_name_label.setText(QCoreApplication.translate("Form", u"{field_name}", None))
    # retranslateUi

