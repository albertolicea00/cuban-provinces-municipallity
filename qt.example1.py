from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

from qt import *

app = QApplication([])
root = QMainWindow()

cb_provinces = QComboBox(root)
cb_municipality = QComboBox(root)
cb_provinces.setGeometry(0,0,200,30)
cb_municipality.setGeometry(0,32,200,30)

# example 1
a = CubaProvinces_BoxGroup(provinceBox = cb_provinces , municipalityBox=cb_municipality)
a.exec()

root.show()
app.exec_()