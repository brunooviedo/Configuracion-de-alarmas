from PyQt5 import QtWidgets, QtGui
from alarma_ui import Ui_MainWindow
datafile = "alarma.ico"

class ventanaprincipal(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(ventanaprincipal,self).__init__()
        self.setWindowIcon(QtGui.QIcon("alarma.ico"))
        self.setupUi(self)
        self.spinBox.valueChanged.connect(self.cuando_spinBox_2_valueChanged)
        self.spinBox_2.valueChanged.connect(self.cuando_SpinBox_valueChanged)

    
        
    def cuando_SpinBox_valueChanged(self, value):
        self.resultado.setText(str(round(((value * 10)/24) * self.spinBox.value(), 1)))

    def cuando_spinBox_2_valueChanged(self, value):
        self.resultado.setText(str(round(((value * 10)/24) * self.spinBox_2.value (), 1)))

    


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    ventanaprincipal = ventanaprincipal()
    ventanaprincipal.show()
    sys.exit(app.exec_())
    