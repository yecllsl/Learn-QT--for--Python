# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QSpinBox, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(589, 370)
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(30, 60, 261, 231))
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(31, 61, 58, 16))
        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(31, 110, 58, 16))
        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(31, 170, 58, 16))
        self.Chinese = QSpinBox(self.groupBox)
        self.Chinese.setObjectName(u"Chinese")
        self.Chinese.setGeometry(QRect(90, 60, 71, 22))
        self.math = QSpinBox(self.groupBox)
        self.math.setObjectName(u"math")
        self.math.setGeometry(QRect(90, 110, 71, 22))
        self.english = QSpinBox(self.groupBox)
        self.english.setObjectName(u"english")
        self.english.setGeometry(QRect(90, 170, 71, 22))
        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(300, 60, 261, 231))
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 90, 58, 16))
        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 150, 58, 16))
        self.total = QLineEdit(self.groupBox_2)
        self.total.setObjectName(u"total")
        self.total.setGeometry(QRect(80, 90, 113, 21))
        self.total.setReadOnly(True)
        self.average = QLineEdit(self.groupBox_2)
        self.average.setObjectName(u"average")
        self.average.setGeometry(QRect(80, 150, 113, 21))
        self.average.setReadOnly(True)
        self.btnCalculate = QPushButton(Form)
        self.btnCalculate.setObjectName(u"btnCalculate")
        self.btnCalculate.setGeometry(QRect(160, 320, 100, 32))
        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")
        self.btnSave.setGeometry(QRect(300, 320, 100, 32))
        self.btnClose = QPushButton(Form)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(420, 320, 100, 32))

        self.retranslateUi(Form)
        self.btnClose.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u6210\u7ee9\uff1a", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8bed\u6587", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6570\u5b66", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u82f1\u8bed", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("Form", u"\u6210\u7ee9\u7edf\u8ba1\uff1a", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u603b\u6210\u7ee9", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u5e73\u5747\u5206", None))
        self.btnCalculate.setText(QCoreApplication.translate("Form", u"\u8ba1\u7b97\u00b7", None))
        self.btnSave.setText(QCoreApplication.translate("Form", u"\u4fdd\u5b58", None))
        self.btnClose.setText(QCoreApplication.translate("Form", u"\u5173\u95ed", None))
    # retranslateUi

