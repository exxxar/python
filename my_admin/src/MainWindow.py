from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import SQL
import sys

from WalletWindow import WalletPanel
from ShopAdminWindow import ShopAdminPanel

class AdminPanel(QtGui.QWidget):

    def __init__(self):
        super(AdminPanel, self).__init__()
        self.initUI()

    def initUI(self):
       # param = self.read_config()
        self.shopAdminBtn = QtGui.QPushButton()
        self.shopAdminBtn.setText("Shop admin")
        self.shopAdminBtn.clicked.connect(self.openShopAdminWindow)
        self.walletAdminBtn = QtGui.QPushButton()
        self.walletAdminBtn.setText("Wallet admin")
        self.walletAdminBtn.clicked.connect(self.openWalletAdminWindow)
        self.sqlAdminBtn = QtGui.QPushButton()
        self.sqlAdminBtn.setText("SQL admin")
        self.sqlAdminBtn.clicked.connect(self.openSqlAdminWindow)
        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)
        self.grid.addWidget(self.shopAdminBtn, 1, 0)
        self.grid.addWidget(self.walletAdminBtn, 2, 0)
        self.grid.addWidget(self.sqlAdminBtn, 3, 0)
        self.setLayout(self.grid)
        self.setGeometry(500, 200, 200, 50)
        self.setWindowTitle('BIG STIRKA ADMIN PANEL')
        self.show()

    def openWalletAdminWindow(self):
        self.walletWindow = WalletPanel()
        self.walletWindow.setMainWindow(self)
        self.walletWindow.show()
        self.setDisabled(True)

    def openShopAdminWindow(self):
        self.shopAdminWindow = ShopAdminPanel()
        self.shopAdminWindow.setMainWindow(self)
        self.shopAdminWindow.show()
        self.setDisabled(True)

    def openSqlAdminWindow(self):
        self.sqlAdminWindow = WalletPanel()
        self.sqlAdminWindow.setMainWindow(self)
        self.sqlAdminWindow.show()
        self.setDisabled(True)

    def closeEvent(self, QCloseEvent):
        sys.exit()



