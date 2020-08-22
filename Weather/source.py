from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from style import Ui_Pogoda
import config
import requests
from bs4 import BeautifulSoup as BS

# 1
app = QtWidgets.QApplication(sys.argv)

# 2
Pogoda = QtWidgets.QDialog()
ui = Ui_Pogoda()
ui.setupUi(Pogoda)
Pogoda.show()

# 3
r = requests.get('https://sinoptik.ua/погода-лондон')
html = BS(r.content, 'html.parser')

for el in html.select('#content'):
    t_min = el.select('.temperature .min')[0].text
    t_max = el.select('.temperature .max')[0].text
    text = el.select('.wDescription .description')[0].text

ui.MIN.setText(t_min)
ui.MAX.setText(t_max)
ui.TEXT.setText(text)


# 4
sys.exit(app.exec_())
