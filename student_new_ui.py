# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'student_new.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QGroupBox, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QSpacerItem, QSpinBox, QVBoxLayout, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(589, 427)
        self.verticalLayout = QVBoxLayout(Form)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_3 = QGroupBox(Form)
        self.groupBox_3.setObjectName(u"groupBox_3")
        self.horizontalLayout = QHBoxLayout(self.groupBox_3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_6 = QLabel(self.groupBox_3)
        self.label_6.setObjectName(u"label_6")

        self.horizontalLayout.addWidget(self.label_6)

        self.name = QLineEdit(self.groupBox_3)
        self.name.setObjectName(u"name")

        self.horizontalLayout.addWidget(self.name)

        self.label_7 = QLabel(self.groupBox_3)
        self.label_7.setObjectName(u"label_7")

        self.horizontalLayout.addWidget(self.label_7)

        self.number = QSpinBox(self.groupBox_3)
        self.number.setObjectName(u"number")
        self.number.setMaximum(10000)

        self.horizontalLayout.addWidget(self.number)

        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(3, 1)

        self.verticalLayout.addWidget(self.groupBox_3)

        self.verticalSpacer = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.groupBox = QGroupBox(Form)
        self.groupBox.setObjectName(u"groupBox")
        self.formLayout = QFormLayout(self.groupBox)
        self.formLayout.setObjectName(u"formLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.Chinese = QSpinBox(self.groupBox)
        self.Chinese.setObjectName(u"Chinese")

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.Chinese)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.math = QSpinBox(self.groupBox)
        self.math.setObjectName(u"math")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.math)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.label_3)

        self.english = QSpinBox(self.groupBox)
        self.english.setObjectName(u"english")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.english)


        self.horizontalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Form)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.formLayout_2 = QFormLayout(self.groupBox_2)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.label_4 = QLabel(self.groupBox_2)
        self.label_4.setObjectName(u"label_4")

        self.formLayout_2.setWidget(0, QFormLayout.LabelRole, self.label_4)

        self.total = QLineEdit(self.groupBox_2)
        self.total.setObjectName(u"total")
        self.total.setReadOnly(True)

        self.formLayout_2.setWidget(0, QFormLayout.FieldRole, self.total)

        self.label_5 = QLabel(self.groupBox_2)
        self.label_5.setObjectName(u"label_5")

        self.formLayout_2.setWidget(1, QFormLayout.LabelRole, self.label_5)

        self.average = QLineEdit(self.groupBox_2)
        self.average.setObjectName(u"average")
        self.average.setReadOnly(True)

        self.formLayout_2.setWidget(1, QFormLayout.FieldRole, self.average)


        self.horizontalLayout_2.addWidget(self.groupBox_2)

        self.horizontalLayout_2.setStretch(0, 1)
        self.horizontalLayout_2.setStretch(1, 1)

        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_2 = QSpacerItem(20, 65, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnCalculate = QPushButton(Form)
        self.btnCalculate.setObjectName(u"btnCalculate")

        self.horizontalLayout_3.addWidget(self.btnCalculate)

        self.btnSave = QPushButton(Form)
        self.btnSave.setObjectName(u"btnSave")

        self.horizontalLayout_3.addWidget(self.btnSave)

        self.btnClose = QPushButton(Form)
        self.btnClose.setObjectName(u"btnClose")

        self.horizontalLayout_3.addWidget(self.btnClose)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Form)
        self.btnClose.clicked.connect(Form.close)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.groupBox_3.setTitle(QCoreApplication.translate("Form", u"\u5b66\u751f\u57fa\u672c\u4fe1\u606f", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u59d3\u540d\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u5b66\u53f7\uff1a", None))
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

