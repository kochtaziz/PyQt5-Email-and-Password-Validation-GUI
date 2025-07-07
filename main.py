from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QApplication

app = QtWidgets.QApplication([])

fen = uic.loadUi("accueil.ui")
fen2 = uic.loadUi("nage.ui")
fen3 = uic.loadUi("resulta.ui")
fen.show()

def generer():
    fen.hide()
    fen2.show()

fen.generer.clicked.connect(generer)

def show():
    fen2.hide()
    fen.show()
    n = fen2.nom.text()
    a = fen2.age.text()
    if len(n) >= 2 and a.isdigit():
        mp = '!!' + a + n[-2:]
        fen.passe.setText(mp)
    else:
        fen.passe.setText("Erreur")

fen2.cree.clicked.connect(show)

def verife():
    ch = fen.mail.text()
    ch1 = fen.passe.text()
    fen.hide()
    fen3.show()
    if "@" not in ch:
        fen3.res.setText("format e-mail invalide")
    elif not ch1.startswith("!!"):
        fen3.res.setText("veuillez verifier ou generer votre mot de passe")
    else:
        fen3.res.setText("bienvenu")

fen.login.clicked.connect(verife)

def false():
    fen3.hide()
    fen.show()

fen3.finn.clicked.connect(false)

app.exec_()
