from PIL import Image
from PIL import ImageDraw
from PIL import ImageFont
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
from email import Encoders
from email.MIMEBase import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import os
import smtplib
import sys
import datetime
from configparser import ConfigParser
import MySQLdb
import os



class SQL:
    db = None
    
    PATH = "dbfiles"
    
    def read_db_config(self,filename='db.ini', section='mysql'):
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
        return 0
    
    def init(self):
        self.connect()
        param = self.read_db_config()
        try:
            sql = 'CREATE DATABASE '+param['database']
            cur = self.db.cursor().execute(sql)
            print cur            
        except Exception as e:
            print "Error in creating db ["+str(e)+"]"
            
        try:
            os.mkdir(self.PATH)
        except OSError as e:
            print e
            
        for i in os.listdir(self.PATH):
            if (i.find(".sql")!=-1):
                f = open(self.PATH+"\\"+i)
                sql = ""
                for k in f.readlines():
                    sql+=k                    
                print sql
                try:  
                    cur = self.db.cursor().execute(sql)
                    print cur
                except Exception as e:
                    print "Error in creating table ["+str(e)+"]"
                    
        self.close()
        return 0
    
    def dropTables(self):
        self.connect()
        try:
            sql = "DROP TABLE items"              
            cur = self.db.cursor().execute(sql)
            print cur
        except Exception as e:
            print "Error in DROP table ["+str(e)+"]"
        
        try:
            sql = "DROP TABLE itemType"              
            cur = self.db.cursor().execute(sql)
            print cur
        except Exception as e:
            print "Error in DROP table ["+str(e)+"]"
        self.close()
        return 0    
    
    def connect(self):
        param = self.read_db_config() 
        
        self.db = MySQLdb.connect(host=param['host'],    # your host, usually localhost
                            user=param['user'],         # your username
                            passwd=param['password'],  # your password
                            db=param['database'])        # name of the data base
        #for row in cur.fetchall():
           # print row[0]
        return 0

    def doBackup(self):
        mass = self.doSQL("SELECT * FROM tab")
        
    def doSQL(self,sqlText):
        try:
            self.connect()

            cur = self.db.cursor()
            cur.execute(sqlText)

            self.close()
            return cur
        except Error as e:
            print e
            self.close()
        return 0
    
    def insert(self):
        sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        return 0
    
    def close(self):
        self.db.close()        
        return 0
    
class Generator(QtGui.QWidget): 
    def __init__(self):
        super(Generator, self).__init__()
        
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
        self.setWindowTitle('BARCODE GENERATOR')    
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Generator()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main() 
#a = SQL()
#a.init()
#a.doSQL("SELECT * FROM tab")