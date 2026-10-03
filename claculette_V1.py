import sys
from PySide6.QtWidgets import QApplication,QWidget,QLabel,QPushButton,QLineEdit,QVBoxLayout,QHBoxLayout,QSpinBox

app=QApplication(sys.argv)
fenetre=QWidget()
fenetre.setWindowTitle("calculette V1")
fenetre.resize(300,300)
layout=QVBoxLayout()
layout_horiz=QHBoxLayout()
layout_horiz2=QHBoxLayout()

message=QLabel("========BIENVENUE DANS MA 1SRT CALCULETTE EN PISYDE6=======",parent=fenetre)
r=QLabel("",parent=fenetre)
egale=QLabel(" = ",parent=fenetre)
N1=QSpinBox(parent=fenetre)
N2=QSpinBox(parent=fenetre)
N1.setMaximum(2000000000)
N2.setMaximum(2000000000)

layout.addWidget(message)
layout_horiz.addWidget(N1)
layout_horiz.addWidget(N2)
layout_horiz.addWidget(egale)
layout_horiz.addWidget(r)
layout.addLayout(layout_horiz)

B_e=QPushButton("C",parent=fenetre)
B_a=QPushButton("+",parent=fenetre)
B_s=QPushButton("-",parent=fenetre)
B_m=QPushButton("x",parent=fenetre)
B_d=QPushButton("/",parent=fenetre)

layout_horiz2.addWidget(B_a)
layout_horiz2.addWidget(B_s)
layout_horiz2.addWidget(B_m)
layout_horiz2.addWidget(B_d)
layout_horiz2.addWidget(B_e)
layout.addLayout(layout_horiz2)


def addition():
    x=N1.value()
    y=N2.value()
    R=x+y
    r.setText(str(R))

def multiplication():
    x=N1.value()
    y=N2.value()
    R=x*y
    r.setText(str(R))

def soustraction():
    x=N1.value()
    y=N2.value()
    R=x-y
    r.setText(str(R))

def division():
    x=N1.value()
    y=N2.value()
    if y==0:
        r.setText("Error(division par 0)")
    else:
        R=x/y
        r.setText(str(round(R,5)))

def erase():
    N1.setValue(0)
    N2.setValue(0)
    r.setText("")
    
B_e.clicked.connect(erase)
B_a.clicked.connect(addition)
B_m.clicked.connect(multiplication)
B_s.clicked.connect(soustraction)
B_d.clicked.connect(division)
fenetre.setLayout(layout)
fenetre.show()
sys.exit(app.exec())
