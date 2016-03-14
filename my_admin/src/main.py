import sys
from PyQt4 import QtGui
from classes.MainWindow import AdminPanel


def main():
    app = QtGui.QApplication(sys.argv)
    mainWin = AdminPanel()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()

#a = SQL()
#a.init()
#a.doSQL("SELECT * FROM tab")