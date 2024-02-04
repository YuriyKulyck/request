import json

import requests
from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()

mainline = QVBoxLayout()

valcodebut = QLineEdit()
valcodebut.setPlaceholderText("valcode:")
datebut = QLineEdit()
datebut.setPlaceholderText("date:")

resultbut = QLabel("result:")
getbut = QPushButton("get source:")

mainline.addWidget(valcodebut)
mainline.addWidget(datebut)
mainline.addWidget(getbut)
mainline.addWidget(resultbut)

window.setLayout(mainline)

def info():
    valcodebut.text()
    datebut.text()
    a = requests.get(f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode={valcodebut.text()}&date={datebut.text()}&json")
    if a.status_code == 200:
        data = json.loads(a.text)
        resultbut.setText(data[0]["txt"] + str(data[0]["rate"]))

getbut.clicked.connect(info)

window.show()
app.exec()
