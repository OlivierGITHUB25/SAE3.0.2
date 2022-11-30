import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QMainWindow, QComboBox, QGridLayout, QMessageBox, QTextBrowser, QTextEdit
import socket

class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        widget = QWidget()
        self.setCentralWidget(widget)
        grid = QGridLayout()
        widget.setLayout(grid)
        self.client_socket = None

        # Titre fenêtre
        self.setWindowTitle("Monitoring")

        # gestion ip serveur
        self.lbl = QLabel(self)
        self.lbl.setText("sélectionner l'ip de votre serveur:")

        self.lbl3 = QLabel(self)
        self.lbl3.setText("IP:")

        self.lbl4 = QLabel(self)
        self.lbl4.setText("PORT:")

        self.champ = QLineEdit(self)
        self.champ3 = QLineEdit(self)

        self.bouton = QPushButton(self)
        self.bouton.setText("Connecter")
        self.bouton.clicked.connect(self.connect)

        self.bouton2 = QPushButton(self)
        self.bouton2.setText("deconnecter")
        self.bouton2.clicked.connect(self.deconnecter)


        # commande
        self.lbl2 = QLabel(self)
        self.lbl2.setText("tapez votre commande:")

        self.champ2 = QLineEdit(self)

        self.bouton3 = QPushButton(self)
        self.bouton3.setText("envoyer")
        self.bouton3.clicked.connect(self.envoyer)


        #Résultat
        self.lbl6 =QLabel(self)
        self.lbl6.setText("Résultat:")
        self.affichage = QTextEdit(self)
        self.affichage.setReadOnly(True)

        #placement
        grid.addWidget(self.lbl3, 1, 2)
        grid.addWidget(self.lbl4, 1, 3)
        grid.addWidget(self.lbl, 2, 1)
        grid.addWidget(self.champ, 2, 2)
        grid.addWidget(self.champ3, 2, 3)
        grid.addWidget(self.bouton, 2, 4)
        grid.addWidget(self.bouton2, 2, 5)
        grid.addWidget(self.lbl2, 3, 1)
        grid.addWidget(self.champ2, 3, 2)
        grid.addWidget(self.bouton3, 3, 3)
        grid.addWidget(self.lbl6, 4, 1)
        grid.addWidget(self.affichage, 5, 1,2,5)

    def connect(self):
        host = self.champ.text()
        port = int(self.champ3.text())
        self.client_socket = socket.socket()
        self.client_socket.connect((host, port))
        self.affichage.append(f"client connecter sur {host} et {port}")

    def envoyer(self):
        msg = self.champ2.text()

        self.client_socket.send(msg.encode())
        data = self.client_socket.recv(1024).decode()
        self.affichage.append(f"{msg}:\n{data}")

    def deconnecter(self):
        msg = "disconect"
        self.client_socket.send(msg.encode())
        self.affichage.append("client deconnecter")






if __name__ == '__main__':

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()