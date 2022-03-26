import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from index import Ui_MainWindow


class LabApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(LabApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.init_UI()
        
    def init_UI(self):
        self.setWindowTitle('Lab One')
        self.ui.pushButton.clicked.connect(self.say_hello)
        self.ui.pushButton_2.clicked.connect(self.say_bye)
        self.ui.pushButton_3.clicked.connect(self.exit)
        
    def say_hello(self):
        print('hello world!')
    
    def say_bye(self):
        print('bye bye')
        
    def exit(self):
        print('app has been closed')
        self.close()
        
app = QtWidgets.QApplication([])
application = LabApp()
application.show()

sys.exit(app.exec())