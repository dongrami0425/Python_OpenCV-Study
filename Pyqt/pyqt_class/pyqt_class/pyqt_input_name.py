import sys
import PyQt5
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi


class Forms(QDialog):
    def __init__(self):  # 생성자
        QDialog.__init__(self,None)
        loadUi('inputname.ui', self)
        self.setWindowTitle('forms PyQt5 Gui')
        self.pushButton.clicked.connect(self.on_pushButton_clicked)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        #self.label1.setText('Welcome:' + self.lineEdit.text())
        self.label1.setText('Welcome:'+self.lineEdit.text()+' '+self.lineEdit2.text())

app = QApplication(sys.argv)
Widget = Forms()
Widget.show()
sys.exit(app.exec_())
