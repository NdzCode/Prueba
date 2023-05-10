
import sys

from PyQt6 import QtCore 
from PyQt6.QtWidgets import QMainWindow,QApplication,QWidget,QLabel,QPushButton,QVBoxLayout,QGridLayout,QTextEdit,QHBoxLayout
from PyQt6.QtGui import *
from PyQt6.QtCore import *


class Ventana(QMainWindow):
    def __init__(self):
        super().__init__()


        self.setWindowTitle("Ventana Grafica")
        self.setFixedSize(QSize(400,200))

# Creando el label y boton de la ventana exterior

        label=QLabel("Nombre Usuario")
        boton=QPushButton("OK") 


# creando el QGridLayout()

        caja_Grid=QGridLayout()

# creando QLabel del Grid de Atributos 
        a01=QLabel("Atributo 1")
        a02=QLabel("Atributo 2")
        a03=QLabel("Atributo 3")
        a04=QLabel("Atributo 4")
        a05=QLabel("Atributo 5")
        a06=QLabel("Atributo 6")

# creando QLabel del Grid de Atributos 
        
        v01=QLabel("Valor 1")
        v02=QLabel("Valor 2")
        v03=QLabel("Valor 3")
        v04=QLabel("Valor 4")
        v05=QLabel("Valor 5")
        v06=QLabel("Valor 6")

        caja_Grid.addWidget(a01,0,0)
        caja_Grid.addWidget(a02,1,0)
        caja_Grid.addWidget(a03,2,0)
        caja_Grid.addWidget(a04,3,0)
        caja_Grid.addWidget(a05,4,0)
        caja_Grid.addWidget(a06,5,0)

        caja_Grid.addWidget(v01,0,1)
        caja_Grid.addWidget(v02,1,1)
        caja_Grid.addWidget(v03,2,1)
        caja_Grid.addWidget(v04,3,1)
        caja_Grid.addWidget(v05,4,1)
        caja_Grid.addWidget(v06,5,1)

        caja=QWidget()
        caja.setLayout(caja_Grid)



# creando el compañero Horizontal del GridLayout()
        
        imagen=QLabel()
        label0=QLabel("Texto descripcion de Usuario")


        ver=QVBoxLayout()

        ver.addWidget(imagen)
        ver.addWidget(label0)
        
        cuadro=QWidget()
        cuadro.setLayout(ver)
       
# Creando el QHBoxLayout() añadiendo cuadro y caja

        horizontal=QHBoxLayout()
        horizontal.addWidget(cuadro)
        horizontal.addWidget(caja)



#Creando el vertical principal

        vertical=QVBoxLayout()
        vertical.addWidget(label)
        vertical.addLayout(horizontal)
        vertical.addWidget(boton)



        ventana=QWidget()
        ventana.setLayout(vertical)
        self.setCentralWidget(ventana)


        
        

        

if __name__=="__main__":
    app=QApplication(sys.argv)
    window=Ventana()
    window.show()
    app.exec()

