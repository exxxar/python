from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import SQL


class ShopAdminPanel(QtGui.QWidget):
    def __init__(self):
        super(ShopAdminPanel, self).__init__()

        self.initUI()

    def initUI(self):
       # param = self.read_config()

        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)

        self.sectionLabel1 = QtGui.QLabel('[Products]')
        self.sectionLabel1.setFont(QtGui.QFont('SansSerif', 15))
        self.grid.addWidget(self.sectionLabel1, 0, 0)

        self.labels1 = []
        self.labels1ProductText = ['id','Code','Name','EM','Count','Price','Type']
        for i in xrange(len(self.labels1ProductText)):
           self.labels1.append(QtGui.QLabel(self.labels1ProductText[i]))
           self.grid.addWidget(self.labels1[i], 1, i)

        self.edits1 = []
        for i in xrange(len(self.labels1ProductText)-1):
           self.edits1.append(QtGui.QLineEdit())
           self.grid.addWidget(self.edits1[i], 2, i)

        self.listType = QComboBox()
        #self.listType.addItems(CODE_TYPES)
        self.edits1[0].setDisabled(True)
        self.grid.addWidget(self.listType, 2, len(self.labels1ProductText)-1)

        self.btns1 = []
        self.btns1Text = ['Add','Remove','Update','Show All']
        for i in xrange(len(self.btns1Text)):
           self.btns1.append(QtGui.QPushButton(self.btns1Text[i]))
           self.grid.addWidget(self.btns1[i], 3, i)
        self.btns1[3].clicked.connect(self.showProductList)

        self.sectionLabel2 = QtGui.QLabel('[Categories]')
        self.sectionLabel2.setFont(QtGui.QFont('SansSerif', 15))
        self.grid.addWidget(self.sectionLabel2, 4, 0)

        self.labels2 = []
        self.labels2ProductText = ['id','TypeName']
        for i in xrange(len(self.labels2ProductText)):
           self.labels2.append(QtGui.QLabel(self.labels2ProductText[i]))
           self.grid.addWidget(self.labels2[i], 5, i)

        self.edits2 = []
        for i in xrange(len(self.labels2ProductText)):
           self.edits2.append(QtGui.QLineEdit())
           self.grid.addWidget(self.edits2[i], 6, i)

        self.edits2[0].setDisabled(True)
        self.btns2 = []
        self.btns2Text = ['Add','Remove','Update','Show All']
        for i in xrange(len(self.btns2Text)):
           self.btns2.append(QtGui.QPushButton(self.btns2Text[i]))
           self.grid.addWidget(self.btns2[i], 7, i)
        self.btns2[3].clicked.connect(self.showCategoryList)

        # Our main window will be a QListView
        self.productList = QListView()
        self.productList.setWindowTitle('Product List')
        self.productList.setMinimumSize(600, 400)

        # Create an empty model for the list's data
        model = QStandardItemModel(self.productList)

        # Add some textual items
        products = [
            'Cookie dough', # Must be store-bought
            'Hummus', # Must be homemade
            'Spaghetti', # Must be saucy
            'Dal makhani', # Must be spicy
            'Chocolate whipped cream' # Must be plentiful
        ]

        for product in products:
            item = QStandardItem(product)
            item.setCheckable(True)
            model.appendRow(item)

        # Apply the model to the list view
        self.productList.setModel(model)
        self.productList.setGeometry(300, 300, 450, 100)


        self.categoryList = QListView()
        self.categoryList.setWindowTitle('Category List')
        self.categoryList.setMinimumSize(200, 100)

        # Create an empty model for the list's data
        model = QStandardItemModel(self.categoryList)

        # Add some textual items
        categoryes = [
            'Cookie dough', # Must be store-bought
            'Hummus', # Must be homemade
            'Spaghetti', # Must be saucy
            'Dal makhani', # Must be spicy
            'Chocolate whipped cream' # Must be plentiful
        ]

        for category in categoryes:
            item = QStandardItem(category)
            item.setCheckable(True)
            model.appendRow(item)

        # Apply the model to the list view
        self.categoryList.setModel(model)
        self.categoryList.setGeometry(300, 300, 150, 100)

        self.setLayout(self.grid)
        self.setGeometry(300, 300, 450, 100)
        self.setWindowTitle('Shop admin')
        self.show()

    def showProductList(self):
        self.productList.show()

    def showCategoryList(self):
        self.categoryList.show()

    def setMainWindow(self,param):
        self.param = param;

    def closeEvent(self, QCloseEvent):
         self.param.setDisabled(False)