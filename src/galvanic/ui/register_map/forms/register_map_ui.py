# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register_map.ui'
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
from PySide6.QtWidgets import (QAbstractScrollArea, QApplication, QHBoxLayout, QLayout,
    QScrollArea, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1426, 517)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.register_map_scrollarea = QScrollArea(Form)
        self.register_map_scrollarea.setObjectName(u"register_map_scrollarea")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.register_map_scrollarea.sizePolicy().hasHeightForWidth())
        self.register_map_scrollarea.setSizePolicy(sizePolicy1)
        self.register_map_scrollarea.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        self.register_map_scrollarea.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustToContents)
        self.register_map_scrollarea.setWidgetResizable(True)
        self.register_map_scrollarea_contents = QWidget()
        self.register_map_scrollarea_contents.setObjectName(u"register_map_scrollarea_contents")
        self.register_map_scrollarea_contents.setGeometry(QRect(0, 0, 24, 505))
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.register_map_scrollarea_contents.sizePolicy().hasHeightForWidth())
        self.register_map_scrollarea_contents.setSizePolicy(sizePolicy2)
        self.register_map_scrollarea_layout = QVBoxLayout(self.register_map_scrollarea_contents)
        self.register_map_scrollarea_layout.setObjectName(u"register_map_scrollarea_layout")
        self.register_map_scrollarea_layout.setSizeConstraint(QLayout.SizeConstraint.SetMinAndMaxSize)
        self.register_map_scrollarea.setWidget(self.register_map_scrollarea_contents)

        self.horizontalLayout.addWidget(self.register_map_scrollarea)


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
    # retranslateUi

