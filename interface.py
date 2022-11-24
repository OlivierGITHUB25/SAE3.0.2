import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QTextBrowser

class MyWindow(QWidget):

    def __init__(self, win):
        super().__init__()
        self.win=win

    def build(self):
        # crée une fenêtre
        self.win.setWindowTitle("Monitoring")
        self.win.setGeometry(100,100,1500, 900)

        # gestion ip serveur
        self.lbl = QLabel(self.win)
        self.lbl.setGeometry(10, 0, 200, 20)
        self.lbl.setText("sélectionner l'ip de votre serveur:")
        self.champ = QLineEdit(self.win)
        self.champ.setGeometry(10, 20, 200, 20)
        self.bouton = QPushButton(self.win)
        self.bouton.setText("Connecter")
        self.bouton.setGeometry(215, 20, 100, 21)
        self.bouton2 = QPushButton(self.win)
        self.bouton2.setText("deconnecter")
        self.bouton2.setGeometry(320, 20, 100, 21)

        # commande
        self.lbl2 = QLabel(self.win)
        self.lbl2.setGeometry(10, 40, 200, 20)
        self.lbl2.setText("tapez votre commande:")
        self.champ2 = QLineEdit(self.win)
        self.champ2.setGeometry(10, 60, 200, 20)
        self.bouton3 = QPushButton(self.win)
        self.bouton3.setText("envoyer")
        self.bouton3.setGeometry(215, 60, 100, 21)

        #Résultat
        self.affichage = QTextBrowser(self.win)
        self.affichage.setGeometry(10, 90, 1000, 500)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    root = QWidget()
    mywin = MyWindow(root)
    mywin.build()

    root.show()
    sys.exit(app.exec_())