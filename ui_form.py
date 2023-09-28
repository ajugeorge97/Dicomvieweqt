# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'form.ui'
##
## Created by: Qt User Interface Compiler version 6.4.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QPushButton,
    QSizePolicy, QSlider, QVBoxLayout, QWidget)

class Ui_Widget(object):
    def setupUi(self, Widget):
        if not Widget.objectName():
            Widget.setObjectName(u"Widget")
        Widget.resize(799, 600)
        self.verticalLayout = QVBoxLayout(Widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header = QFrame(Widget)
        self.header.setObjectName(u"header")
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.header)

        self.body = QFrame(Widget)
        self.body.setObjectName(u"body")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.body)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.frame = QFrame(self.body)
        self.frame.setObjectName(u"frame")
        self.frame.setMinimumSize(QSize(300, 0))
        self.frame.setMaximumSize(QSize(300, 16777215))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")

        self.horizontalLayout_3.addWidget(self.pushButton_2, 0, Qt.AlignRight|Qt.AlignBottom)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.horizontalLayout.addWidget(self.frame)

        self.viewer = QFrame(self.body)
        self.viewer.setObjectName(u"viewer")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.viewer.sizePolicy().hasHeightForWidth())
        self.viewer.setSizePolicy(sizePolicy1)
        self.viewer.setFrameShape(QFrame.StyledPanel)
        self.viewer.setFrameShadow(QFrame.Raised)

        self.horizontalLayout.addWidget(self.viewer)

        self.frame_3 = QFrame(self.body)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(30, 16777215))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, -1, 0, -1)
        self.verticalSlider2 = QSlider(self.frame_3)
        self.verticalSlider2.setObjectName(u"verticalSlider2")
        self.verticalSlider2.setOrientation(Qt.Vertical)

        self.horizontalLayout_2.addWidget(self.verticalSlider2)


        self.horizontalLayout.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.body)


        self.retranslateUi(Widget)

        QMetaObject.connectSlotsByName(Widget)
    # setupUi

    def retranslateUi(self, Widget):
        Widget.setWindowTitle(QCoreApplication.translate("Widget", u"Widget", None))
        self.pushButton_2.setText(QCoreApplication.translate("Widget", u"PushButton", None))
    # retranslateUi

