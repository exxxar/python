from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import SQL


class WalletPanel(QtGui.QWidget):
    def __init__(self):
        super(WalletPanel, self).__init__()

        self.initUI()

    def initUI(self):
       # param = self.read_config()

        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)
        self.view = QtGui.QTableView()


        sort = QtGui.QSortFilterProxyModel()
        model = QtGui.QStandardItemModel(4, 6)
        model.setHorizontalHeaderLabels( ['id', 'Phone', 'Email', 'Product','Count','Price'])
        pr = QtGui.QStandardItem()
        pr.setData(QtCore.QVariant("SDDASD"), QtCore.Qt.DisplayRole)
        pr.setEditable(False)

        pr1 = QtGui.QStandardItem()
        pr1.setData(QtCore.QVariant("SDDASD2"), QtCore.Qt.DisplayRole)
        pr1.setEditable(False)

        model.insertRow(0, [pr,pr1])
        model.insertRow(1, [pr])
        model.insertRow(2, [pr])

        sort.setSourceModel(model)
        self.view.setModel(sort)
        self.grid.addWidget(self.view,0 , 0)

        self.btns = []
        self.btnText = ['Accept','Remove','Clear']
        for i in xrange(len(self.btnText)):
           self.btns.append(QtGui.QPushButton(self.btnText[i]))
           self.grid.addWidget(self.btns[i],  i+1,0)

        self.setLayout(self.grid)
        self.setGeometry(300, 300, 670, 500)
        self.setWindowTitle('Wallet window')
        self.show()

    def setMainWindow(self,param):
        self.param = param;

    def closeEvent(self, QCloseEvent):
         self.param.setDisabled(False)