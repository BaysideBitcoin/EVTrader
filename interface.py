# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'interface.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(301, 363)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.sellButton = QtWidgets.QPushButton(self.centralwidget)
        self.sellButton.setGeometry(QtCore.QRect(160, 320, 131, 31))
        self.sellButton.setObjectName("sellButton")
        self.buyButton = QtWidgets.QPushButton(self.centralwidget)
        self.buyButton.setGeometry(QtCore.QRect(10, 320, 131, 31))
        self.buyButton.setObjectName("buyButton")
        self.askListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.askListWidget.setGeometry(QtCore.QRect(80, 180, 141, 91))
        self.askListWidget.setObjectName("askListWidget")
        self.bidListWidget = QtWidgets.QListWidget(self.centralwidget)
        self.bidListWidget.setGeometry(QtCore.QRect(80, 70, 141, 91))
        self.bidListWidget.setObjectName("bidListWidget")
        self.sellLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.sellLineEdit.setGeometry(QtCore.QRect(160, 280, 131, 31))
        self.sellLineEdit.setObjectName("sellLineEdit")
        self.marketComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.marketComboBox.setGeometry(QtCore.QRect(49, 10, 241, 21))
        self.marketComboBox.setObjectName("marketComboBox")
        self.marketComboBox.addItem("")
        self.marketComboBox.addItem("")
        self.marketComboBox.addItem("")
        self.marketComboBox.addItem("")
        self.marketLabel = QtWidgets.QLabel(self.centralwidget)
        self.marketLabel.setGeometry(QtCore.QRect(10, 10, 33, 16))
        self.marketLabel.setObjectName("marketLabel")
        self.buyLineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.buyLineEdit.setGeometry(QtCore.QRect(10, 280, 131, 31))
        self.buyLineEdit.setObjectName("buyLineEdit")
        self.usdHeldValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.usdHeldValueLabel.setGeometry(QtCore.QRect(160, 31, 131, 20))
        self.usdHeldValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.usdHeldValueLabel.setObjectName("usdHeldValueLabel")
        self.coinsHeldValueLabel = QtWidgets.QLabel(self.centralwidget)
        self.coinsHeldValueLabel.setGeometry(QtCore.QRect(160, 50, 131, 20))
        self.coinsHeldValueLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.coinsHeldValueLabel.setObjectName("coinsHeldValueLabel")
        self.currentCoinPrice = QtWidgets.QLabel(self.centralwidget)
        self.currentCoinPrice.setGeometry(QtCore.QRect(80, 161, 141, 16))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.currentCoinPrice.setFont(font)
        self.currentCoinPrice.setAlignment(QtCore.Qt.AlignCenter)
        self.currentCoinPrice.setObjectName("currentCoinPrice")
        self.orderComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.orderComboBox.setGeometry(QtCore.QRect(80, 40, 71, 21))
        self.orderComboBox.setObjectName("orderComboBox")
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderComboBox.addItem("")
        self.orderLabel = QtWidgets.QLabel(self.centralwidget)
        self.orderLabel.setGeometry(QtCore.QRect(10, 40, 61, 16))
        self.orderLabel.setObjectName("orderLabel")
        self.debugLabel_2 = QtWidgets.QLabel(self.centralwidget)
        self.debugLabel_2.setGeometry(QtCore.QRect(50, 110, 21, 16))
        self.debugLabel_2.setObjectName("debugLabel_2")
        self.debugLabel_3 = QtWidgets.QLabel(self.centralwidget)
        self.debugLabel_3.setGeometry(QtCore.QRect(50, 210, 21, 16))
        self.debugLabel_3.setObjectName("debugLabel_3")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(150, 280, 3, 70))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 301, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "- EVTrader"))
        self.sellButton.setText(_translate("MainWindow", "Sell"))
        self.buyButton.setText(_translate("MainWindow", "Buy"))
        self.marketComboBox.setItemText(0, _translate("MainWindow", "GDAX Bitcoin (BTC/USD)"))
        self.marketComboBox.setItemText(1, _translate("MainWindow", "GDAX Litecoin (LTC/USD)"))
        self.marketComboBox.setItemText(2, _translate("MainWindow", "GDAX Ethereum (ETH/USD)"))
        self.marketComboBox.setItemText(3, _translate("MainWindow", "GDAX Bitcoin Cash (BCC/USD)"))
        self.marketLabel.setText(_translate("MainWindow", "Market"))
        self.usdHeldValueLabel.setText(_translate("MainWindow", "0"))
        self.coinsHeldValueLabel.setText(_translate("MainWindow", "0"))
        self.currentCoinPrice.setText(_translate("MainWindow", "0"))
        self.orderComboBox.setItemText(0, _translate("MainWindow", "Undercut"))
        self.orderComboBox.setItemText(1, _translate("MainWindow", "Market"))
        self.orderComboBox.setItemText(2, _translate("MainWindow", "Limit"))
        self.orderComboBox.setItemText(3, _translate("MainWindow", "Stop"))
        self.orderLabel.setText(_translate("MainWindow", "Order Type"))
        self.debugLabel_2.setText(_translate("MainWindow", "Asks"))
        self.debugLabel_3.setText(_translate("MainWindow", "Bids"))
