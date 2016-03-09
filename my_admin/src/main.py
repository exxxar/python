from MainWindow import AdminPanel
from PyQt4 import QtCore
from PyQt4 import QtGui
from PyQt4.QtGui import *
import sys



def main():

    app = QtGui.QApplication(sys.argv)

    mainWin = AdminPanel()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
#a = SQL()
#a.init()
#a.doSQL("SELECT * FROM tab")