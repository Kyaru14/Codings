# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'designerpZXQro.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(974, 634)
        MainWindow.setMinimumSize(QSize(974, 634))
        MainWindow.setMaximumSize(QSize(974, 634))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.tabWidget = QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setGeometry(QRect(0, 0, 961, 441))
        self.huffman_widget = QWidget()
        self.huffman_widget.setObjectName(u"huffman_widget")
        self.msgbox_h = QPlainTextEdit(self.huffman_widget)
        self.msgbox_h.setObjectName(u"msgbox_h")
        self.msgbox_h.setGeometry(QRect(50, 40, 481, 121))
        font = QFont()
        font.setPointSize(12)
        self.msgbox_h.setFont(font)
        self.label = QLabel(self.huffman_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(50, 10, 71, 20))
        self.label_2 = QLabel(self.huffman_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(90, 170, 71, 21))
        self.n_box = QLineEdit(self.huffman_widget)
        self.n_box.setObjectName(u"n_box")
        self.n_box.setGeometry(QRect(50, 170, 31, 20))
        self.r_box = QLineEdit(self.huffman_widget)
        self.r_box.setObjectName(u"r_box")
        self.r_box.setGeometry(QRect(150, 170, 31, 20))
        self.label_3 = QLabel(self.huffman_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 170, 51, 21))
        self.coding_result_box_h = QPlainTextEdit(self.huffman_widget)
        self.coding_result_box_h.setObjectName(u"coding_result_box_h")
        self.coding_result_box_h.setGeometry(QRect(620, 40, 301, 191))
        font1 = QFont()
        font1.setFamily(u"\u5b8b\u4f53")
        font1.setPointSize(12)
        self.coding_result_box_h.setFont(font1)
        self.label_4 = QLabel(self.huffman_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(620, 15, 111, 21))
        self.encoded_box_h = QPlainTextEdit(self.huffman_widget)
        self.encoded_box_h.setObjectName(u"encoded_box_h")
        self.encoded_box_h.setGeometry(QRect(50, 250, 481, 131))
        self.encoded_box_h.setFont(font)
        self.label_5 = QLabel(self.huffman_widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(50, 220, 81, 20))
        self.encode_button_h = QPushButton(self.huffman_widget)
        self.encode_button_h.setObjectName(u"encode_button_h")
        self.encode_button_h.setGeometry(QRect(230, 190, 75, 31))
        self.label_6 = QLabel(self.huffman_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(620, 240, 81, 21))
        self.summary_box_h = QPlainTextEdit(self.huffman_widget)
        self.summary_box_h.setObjectName(u"summary_box_h")
        self.summary_box_h.setGeometry(QRect(620, 270, 301, 111))
        self.decode_button_h = QPushButton(self.huffman_widget)
        self.decode_button_h.setObjectName(u"decode_button_h")
        self.decode_button_h.setGeometry(QRect(320, 190, 75, 31))
        self.tabWidget.addTab(self.huffman_widget, "")
        self.shannon_widget = QWidget()
        self.shannon_widget.setObjectName(u"shannon_widget")
        self.msgbox_s = QPlainTextEdit(self.shannon_widget)
        self.msgbox_s.setObjectName(u"msgbox_s")
        self.msgbox_s.setGeometry(QRect(50, 40, 481, 141))
        self.msgbox_s.setFont(font)
        self.encoded_box_s = QPlainTextEdit(self.shannon_widget)
        self.encoded_box_s.setObjectName(u"encoded_box_s")
        self.encoded_box_s.setGeometry(QRect(50, 250, 481, 131))
        self.encoded_box_s.setFont(font)
        self.encode_button_s = QPushButton(self.shannon_widget)
        self.encode_button_s.setObjectName(u"encode_button_s")
        self.encode_button_s.setGeometry(QRect(140, 190, 75, 31))
        self.coding_result_box_s = QPlainTextEdit(self.shannon_widget)
        self.coding_result_box_s.setObjectName(u"coding_result_box_s")
        self.coding_result_box_s.setGeometry(QRect(620, 40, 301, 191))
        self.coding_result_box_s.setFont(font1)
        self.label_10 = QLabel(self.shannon_widget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(620, 240, 81, 21))
        self.summary_box_s = QPlainTextEdit(self.shannon_widget)
        self.summary_box_s.setObjectName(u"summary_box_s")
        self.summary_box_s.setGeometry(QRect(620, 270, 301, 111))
        self.label_11 = QLabel(self.shannon_widget)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(50, 220, 81, 20))
        self.label_12 = QLabel(self.shannon_widget)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(620, 15, 111, 21))
        self.label_13 = QLabel(self.shannon_widget)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(50, 10, 71, 20))
        self.decode_button_s = QPushButton(self.shannon_widget)
        self.decode_button_s.setObjectName(u"decode_button_s")
        self.decode_button_s.setGeometry(QRect(330, 190, 75, 31))
        self.tabWidget.addTab(self.shannon_widget, "")
        self.fino_widget = QWidget()
        self.fino_widget.setObjectName(u"fino_widget")
        self.msgbox_f = QPlainTextEdit(self.fino_widget)
        self.msgbox_f.setObjectName(u"msgbox_f")
        self.msgbox_f.setGeometry(QRect(50, 40, 481, 141))
        self.msgbox_f.setFont(font)
        self.encoded_box_f = QPlainTextEdit(self.fino_widget)
        self.encoded_box_f.setObjectName(u"encoded_box_f")
        self.encoded_box_f.setGeometry(QRect(50, 250, 481, 131))
        self.encoded_box_f.setFont(font)
        self.encode_button_f = QPushButton(self.fino_widget)
        self.encode_button_f.setObjectName(u"encode_button_f")
        self.encode_button_f.setGeometry(QRect(140, 190, 75, 31))
        self.coding_result_box_f = QPlainTextEdit(self.fino_widget)
        self.coding_result_box_f.setObjectName(u"coding_result_box_f")
        self.coding_result_box_f.setGeometry(QRect(620, 40, 301, 191))
        self.coding_result_box_f.setFont(font1)
        self.label_16 = QLabel(self.fino_widget)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(620, 240, 81, 21))
        self.summary_box_f = QPlainTextEdit(self.fino_widget)
        self.summary_box_f.setObjectName(u"summary_box_f")
        self.summary_box_f.setGeometry(QRect(620, 270, 301, 111))
        self.label_17 = QLabel(self.fino_widget)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(50, 220, 81, 20))
        self.label_18 = QLabel(self.fino_widget)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setGeometry(QRect(620, 15, 111, 21))
        self.label_19 = QLabel(self.fino_widget)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setGeometry(QRect(50, 10, 71, 20))
        self.decode_button_f = QPushButton(self.fino_widget)
        self.decode_button_f.setObjectName(u"decode_button_f")
        self.decode_button_f.setGeometry(QRect(330, 190, 75, 31))
        self.tabWidget.addTab(self.fino_widget, "")
        self.console_box = QPlainTextEdit(self.centralwidget)
        self.console_box.setObjectName(u"console_box")
        self.console_box.setGeometry(QRect(10, 460, 951, 151))
        font2 = QFont()
        font2.setPointSize(10)
        self.console_box.setFont(font2)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(10, 440, 81, 18))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", u"\u4fe1\u606f\u8bba\u8bfe\u7a0b\u8bbe\u8ba1", None))
        self.huffman_widget.setProperty("title",
                                        QCoreApplication.translate("MainWindow", u"\u970d\u592b\u66fc\u7f16\u7801",
                                                                   None))
        self.msgbox_h.setPlainText(QCoreApplication.translate("MainWindow",
                                                              u"Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream.",
                                                              None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u5185\u5bb9", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u5e8f\u5217", None))
        self.n_box.setText(QCoreApplication.translate("MainWindow", u"1", None))
        self.r_box.setText(QCoreApplication.translate("MainWindow", u"2", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u5236", None))
        self.coding_result_box_h.setPlainText("")
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"\u7801\u5b57\u5bf9\u5e94\u5173\u7cfb", None))
        self.encoded_box_h.setPlainText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7ed3\u679c", None))
        self.encode_button_h.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u6027\u80fd", None))
        self.summary_box_h.setPlainText(QCoreApplication.translate("MainWindow", u"\u4fe1\u6e90\u71b5\uff1a\n"
                                                                                 "\u5e73\u5747\u7801\u957f\uff1a\n"
                                                                                 "\u7f16\u7801\u6548\u7387\uff1a\n"
                                                                                 "\u538b\u7f29\u7387\uff1a", None))
        self.decode_button_h.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.huffman_widget),
                                  QCoreApplication.translate("MainWindow", u"\u970d\u592b\u66fc\u7f16\u7801", None))
        self.msgbox_s.setPlainText(QCoreApplication.translate("MainWindow",
                                                              u"Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream.",
                                                              None))
        self.encoded_box_s.setPlainText("")
        self.encode_button_s.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u6027\u80fd", None))
        self.summary_box_s.setPlainText(QCoreApplication.translate("MainWindow", u"\u4fe1\u6e90\u71b5\uff1a\n"
                                                                                 "\u5e73\u5747\u7801\u957f\uff1a\n"
                                                                                 "\u7f16\u7801\u6548\u7387\uff1a\n"
                                                                                 "\u538b\u7f29\u7387\uff1a", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7ed3\u679c", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"\u7801\u5b57\u5bf9\u5e94\u5173\u7cfb", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u5185\u5bb9", None))
        self.decode_button_s.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.shannon_widget),
                                  QCoreApplication.translate("MainWindow", u"\u9999\u519c\u7f16\u7801", None))
        self.msgbox_f.setPlainText(QCoreApplication.translate("MainWindow",
                                                              u"Prints the values to a stream, or to sys.stdout by default. Optional keyword arguments: file: a file-like object (stream); defaults to the current sys.stdout. sep: string inserted between values, default a space. end: string appended after the last value, default a newline. flush: whether to forcibly flush the stream.",
                                                              None))
        self.encoded_box_f.setPlainText("")
        self.encode_button_f.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u6027\u80fd", None))
        self.summary_box_f.setPlainText(QCoreApplication.translate("MainWindow", u"\u4fe1\u6e90\u71b5\uff1a\n"
                                                                                 "\u5e73\u5747\u7801\u957f\uff1a\n"
                                                                                 "\u7f16\u7801\u6548\u7387\uff1a\n"
                                                                                 "\u538b\u7f29\u7387\uff1a", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u7ed3\u679c", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"\u7801\u5b57\u5bf9\u5e94\u5173\u7cfb", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"\u7f16\u7801\u5185\u5bb9", None))
        self.decode_button_f.setText(QCoreApplication.translate("MainWindow", u"\u89e3\u7801", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.fino_widget),
                                  QCoreApplication.translate("MainWindow", u"\u8d39\u8bfa\u7f16\u7801", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Console", None))
    # retranslateUi
