from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import SQL
import sys

from WalletWindow import WalletPanel
from ShopAdminWindow import ShopAdminPanel

class SqlPanel(QtGui.QWidget):

    def __init__(self):
        super(SqlPanel, self).__init__()
        self.initUI()

    def initUI(self):
       # param = self.read_config()
        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)

        self.btns = []
        self.btnText = ['Create','Backup','AutoFill','DropTables','ClearData']
        for i in xrange(len(self.btnText)):
           self.btns.append(QtGui.QPushButton(self.btnText[i]))
           self.grid.addWidget(self.btns[i], i, 0)


        self.setGeometry(500, 200, 200, 50)
        self.setWindowTitle('SQL-panel')
        self.show()


    def setMainWindow(self,param):
        self.param = param;

    def closeEvent(self, QCloseEvent):
         self.param.setDisabled(False)


