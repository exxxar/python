from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import SQL
from configparser import ConfigParser

class ConfigPanel(QtGui.QWidget):
    def __init__(self):
        super(ConfigPanel, self).__init__()

        self.initUI()

    def read_config(self,filename='db.ini', section='mysql'):
        try:
            parser = ConfigParser()
            parser.read(filename)

            # get section, default to mysql
            params = {}
            if parser.has_section(section):
                items = parser.items(section)
                for item in items:
                    params[item[0]] = item[1]
            else:
                raise Exception('{0} not found in the {1} file'.format(section, filename))
            return params
        except Exception as e:
            print e

    def initUI(self):
        param = self.read_config()
        self.sectionLabel = QtGui.QLabel('[MySQL]')
        self.sectionLabel.setFont(QtGui.QFont('SansSerif', 15))

        self.grid = QtGui.QGridLayout(self)
        self.grid.setSpacing(20)
        self.grid.addWidget(self.sectionLabel, 2, 1)
        self.labels = []
        self.lebelText = ['Host','Database','User','Password','Tables','Backups','XLS']
        for i in xrange(len(self.lebelText)):
           self.labels.append(QtGui.QLabel(self.lebelText[i]))
           self.grid.addWidget(self.labels[i], i+3, 0)

        self.edits = []
        for i in xrange(len(self.lebelText)):
           edit = QtGui.QLineEdit()
           edit.setText(param[self.lebelText[i].lower()] if param!=None and self.lebelText[i].lower() in param else "")
           self.edits.append(edit)
           self.grid.addWidget(self.edits[i], i+3, 1)

        self.image = QtGui.QLabel("window")
        self.image.setGeometry(10, 10, 200, 400)
        self.image.setPixmap(QtGui.QPixmap("img/settings.png"))
        self.grid.addWidget(self.image, 1, 1)

        self.submit = QtGui.QPushButton()
        self.submit.setText("SAVE")
        self.grid.addWidget(self.submit,len(self.lebelText)+4 , 1)
        self.submit.clicked.connect(self.saveParams)

        self.setLayout(self.grid)
        self.setGeometry(300, 300, 250, 100)
        self.setWindowTitle('SETTINGS')
        self.show()

    def saveParams(self):
       cfgfile = open("db.ini",'w')
       Config = ConfigParser()
       Config.add_section('mysql')
       for i in xrange(len(self.lebelText)):
           Config.set('mysql',self.lebelText[i],str(self.edits[i].text()))
       Config.write(cfgfile)
       cfgfile.close()

    def setMainWindow(self,param):
        self.param = param;

    def closeEvent(self, QCloseEvent):
         self.param.setDisabled(False)