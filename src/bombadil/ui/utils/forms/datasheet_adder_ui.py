# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'datasheet_adder.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 352)
        self.main_layout = QVBoxLayout(Form)
        self.main_layout.setSpacing(10)
        self.main_layout.setObjectName(u"main_layout")
        self.main_layout.setContentsMargins(10, 10, 10, 10)
        self.title_label = QLabel(Form)
        self.title_label.setObjectName(u"title_label")
        font = QFont()
        font.setPointSize(14)
        font.setBold(True)
        self.title_label.setFont(font)

        self.main_layout.addWidget(self.title_label)

        self.drop_frame = QFrame(Form)
        self.drop_frame.setObjectName(u"drop_frame")
        self.drop_frame.setMinimumSize(QSize(0, 120))
        self.drop_frame.setFrameShape(QFrame.NoFrame)
        self.drop_frame.setLineWidth(2)
        self.drop_frame_layout = QVBoxLayout(self.drop_frame)
        self.drop_frame_layout.setObjectName(u"drop_frame_layout")
        self.drop_label = QLabel(self.drop_frame)
        self.drop_label.setObjectName(u"drop_label")
        font1 = QFont()
        font1.setPointSize(11)
        self.drop_label.setFont(font1)

        self.drop_frame_layout.addWidget(self.drop_label)

        self.or_label = QLabel(self.drop_frame)
        self.or_label.setObjectName(u"or_label")

        self.drop_frame_layout.addWidget(self.or_label)

        self.browse_layout = QHBoxLayout()
        self.browse_layout.setObjectName(u"browse_layout")
        self.browse_spacer_left = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.browse_layout.addItem(self.browse_spacer_left)

        self.browse_pushbutton = QPushButton(self.drop_frame)
        self.browse_pushbutton.setObjectName(u"browse_pushbutton")

        self.browse_layout.addWidget(self.browse_pushbutton)

        self.browse_spacer_right = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.browse_layout.addItem(self.browse_spacer_right)


        self.drop_frame_layout.addLayout(self.browse_layout)


        self.main_layout.addWidget(self.drop_frame)

        self.selected_file_label = QLabel(Form)
        self.selected_file_label.setObjectName(u"selected_file_label")

        self.main_layout.addWidget(self.selected_file_label)

        self.url_layout = QHBoxLayout()
        self.url_layout.setObjectName(u"url_layout")
        self.url_label = QLabel(Form)
        self.url_label.setObjectName(u"url_label")

        self.url_layout.addWidget(self.url_label)

        self.url_lineedit = QLineEdit(Form)
        self.url_lineedit.setObjectName(u"url_lineedit")

        self.url_layout.addWidget(self.url_lineedit)


        self.main_layout.addLayout(self.url_layout)

        self.name_layout = QHBoxLayout()
        self.name_layout.setObjectName(u"name_layout")
        self.name_label = QLabel(Form)
        self.name_label.setObjectName(u"name_label")

        self.name_layout.addWidget(self.name_label)

        self.part_number_lineedit = QLineEdit(Form)
        self.part_number_lineedit.setObjectName(u"part_number_lineedit")

        self.name_layout.addWidget(self.part_number_lineedit)


        self.main_layout.addLayout(self.name_layout)

        self.autocreate_json_checkbox = QCheckBox(Form)
        self.autocreate_json_checkbox.setObjectName(u"autocreate_json_checkbox")
        self.autocreate_json_checkbox.setChecked(True)

        self.main_layout.addWidget(self.autocreate_json_checkbox)

        self.bottom_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.main_layout.addItem(self.bottom_spacer)

        self.button_layout = QHBoxLayout()
        self.button_layout.setObjectName(u"button_layout")
        self.button_spacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.button_layout.addItem(self.button_spacer)

        self.cancel_pushbutton = QPushButton(Form)
        self.cancel_pushbutton.setObjectName(u"cancel_pushbutton")

        self.button_layout.addWidget(self.cancel_pushbutton)

        self.create_pushbutton = QPushButton(Form)
        self.create_pushbutton.setObjectName(u"create_pushbutton")
        self.create_pushbutton.setEnabled(False)

        self.button_layout.addWidget(self.create_pushbutton)


        self.main_layout.addLayout(self.button_layout)

        self.status_label = QLabel(Form)
        self.status_label.setObjectName(u"status_label")

        self.main_layout.addWidget(self.status_label)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Add Datasheet", None))
        self.title_label.setText(QCoreApplication.translate("Form", u"Add Component Datasheet", None))
        self.drop_label.setText(QCoreApplication.translate("Form", u"Drag and drop PDF or MD file here", None))
        self.or_label.setText(QCoreApplication.translate("Form", u"- or -", None))
        self.browse_pushbutton.setText(QCoreApplication.translate("Form", u"Browse...", None))
        self.selected_file_label.setText(QCoreApplication.translate("Form", u"No file selected", None))
        self.url_label.setText(QCoreApplication.translate("Form", u"URL:", None))
        self.url_lineedit.setPlaceholderText(QCoreApplication.translate("Form", u"https://example.com/datasheet.pdf", None))
        self.name_label.setText(QCoreApplication.translate("Form", u"Part Number:", None))
        self.part_number_lineedit.setPlaceholderText(QCoreApplication.translate("Form", u"e.g., stm32f103", None))
        self.autocreate_json_checkbox.setText(QCoreApplication.translate("Form", u"Auto-create JSON (parse datasheet)", None))
        self.cancel_pushbutton.setText(QCoreApplication.translate("Form", u"Cancel", None))
        self.create_pushbutton.setText(QCoreApplication.translate("Form", u"Create Datasheet", None))
        self.status_label.setText("")
    # retranslateUi

