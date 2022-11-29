import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton

def action():
    text = qline.text()
    print("tu fais quoi")
    mylabel.setText("tu fais quoi")


app = QApplication(sys.argv)

win = QWidget()
win.setWindowTitle("mon app")
win.setGeometry(100, 100, 600, 300)

mylabel = QLabel(win)
mylabel.setText(action(text))
# mylabel.setGeometry(220, 100, 300, 50)

qline = QLineEdit(win)
qline.setGeometry(50, 100, 150, 20)
qline.textChanged.connect(action)

qBTN = QPushButton(win)
qBTN.setText("push moi")
qBTN.setGeometry(100, 100, 200, 30)
qBTN.clicked.connect(action)



win.show()
sys.exit(app.exec_())


