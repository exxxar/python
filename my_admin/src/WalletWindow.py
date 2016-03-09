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
        self.codeS_title = QtGui.QLabel('Type')
        self.title = QtGui.QLabel('Country')
        self.author = QtGui.QLabel('ID')
        self.review = QtGui.QLabel('Count')
        self.price = QtGui.QLabel('Price')
        self.email = QtGui.QLabel('Email')
        self.contryEdit = QtGui.QLineEdit()
        self.contryEdit.setText(str("fsdfs"))
        self.idEdit = QtGui.QLineEdit()
        self.idEdit.setText(str("param['id']"))
        self.log = QtGui.QTextEdit()
        self.countEdit = QtGui.QLineEdit()
        self.countEdit.setText(str("param['count']"))
        self.priceEdit = QtGui.QLineEdit()
        self.priceEdit.setText(str("param['price']"))
        self.emailEdit = QtGui.QLineEdit()
        self.emailEdit.setText(str("param['email']"))
        self.image = QtGui.QLabel("window")
        self.image.setGeometry(10, 10, 200, 400)
        self.image.setPixmap(QtGui.QPixmap("barcode_scanner_icon.png"))
        self.button = QtGui.QPushButton()
        self.button.setText("GENERATE")
        #self.button.clicked.connect(self.handleButton)
        self.toHtml = QtGui.QPushButton()
        self.toHtml.setText("SEND")
        #self.toHtml.clicked.connect(self.toHTML)
        self.clear = QtGui.QPushButton()
        self.clear.setText("HELP")
        #self.clear.clicked.connect(self.HELPMe)
        self.watermark = QtGui.QPushButton()
        self.watermark.setText("Watermark")
        #self.watermark.clicked.connect(self.addWaterMark)
        self.progress = QtGui.QProgressBar();
        self.progress.setMaximum(0)
        self.progress.setMinimum(0)
        self.progress.setValue(0)
        self.listWidget = QComboBox()
        #self.listWidget.addItems(CODE_TYPES)
        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)
        self.listWidget = QComboBox()
        #self.listWidget.addItems(CODE_TYPES)
        self.grid.addWidget(self.image, 1, 1)
        self.grid.addWidget(self.codeS_title, 2, 0)
        self.grid.addWidget(self.listWidget, 2, 1)
        self.grid.addWidget(self.title, 3, 0)
        self.grid.addWidget(self.contryEdit, 3, 1)
        self.grid.addWidget(self.author, 4, 0)
        self.grid.addWidget(self.idEdit, 4, 1)
        self.grid.addWidget(self.review, 5, 0)
        self.grid.addWidget(self.countEdit, 5, 1)
        self.grid.addWidget(self.price, 6, 0)
        self.grid.addWidget(self.priceEdit, 6, 1)
        self.grid.addWidget(self.email, 7, 0)
        self.grid.addWidget(self.emailEdit, 7, 1)
        self.grid.addWidget(self.button, 8, 1)
        self.grid.addWidget(self.progress, 9, 1)
        self.grid.addWidget(self.log, 10, 1, 5, 1)
        self.grid.addWidget(self.toHtml, 11, 0)
        self.grid.addWidget(self.watermark, 12, 0)
        self.grid.addWidget(self.clear, 13, 0)
        self.setLayout(self.grid)
        self.setGeometry(300, 300, 450, 100)
        self.setWindowTitle('BARCODE GENERATORasdasdasdasd')
        self.show()

    def setMainWindow(self,param):
        self.param = param;

    def closeEvent(self, QCloseEvent):
         self.param.setDisabled(False)