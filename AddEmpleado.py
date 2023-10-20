import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow


class Addemple1(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(Addemple1,self).__init__()

        self.setWindowTitle("Agregar Empleado")

        # Poner el color  de fondo a la ventana
        self.setStyleSheet("background-color: #EDEDED;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 500
        self.alto = 400

        # Establecer el tamaño de la ventana:
        self.resize(self.ancho, self.alto)

        # Estas lineas hacen que la ventana se vea en el centro:
        self.pantalla = self.frameGeometry()
        self.centro = QDesktopWidget().availableGeometry().center()
        self.pantalla.moveCenter(self.centro)
        self.move(self.pantalla.topLeft())

        # Para que la ventana no se pueda cambiar de tamaño
        # Se fija el ancho y el alto
        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)

        self.setStyleSheet("background-color: White;")

        # Hacemos el tipo de letra
        self.letra1 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra1.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra1.setPointSize(10)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(12)



        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Nombre:")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(200)

        self.login.move(50, 100)

        # Hacemos el campo para ingresar el primer numero
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(300)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editLogin.setMaxLength(20)

        self.editLogin.move(50, 150)

        # Hacemos el letrero
        self.contraseña = QLabel(self)
        # Le escribimos el texto
        self.contraseña.setText("Puesto:")
        # Le asignamos el tipo de letra
        self.contraseña.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.contraseña.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.contraseña.setFixedWidth(200)

        self.contraseña.move(50, 200)

        # Hacemos el campo para ingresar el primer numero
        self.editContraseña = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editContraseña.setFixedWidth(300)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editContraseña.setMaxLength(20)

        self.editContraseña.move(50, 240)

        # Hacemos un boton para hacer los calculos
        self.botonCalcular = QPushButton(self)
        self.botonCalcular.setText("Agregar Empleado")
        # Establecemos el ancho del boton
        self.botonCalcular.setFixedWidth(300)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.botonCalcular.setStyleSheet("background-color: #FF66FF; color: #000000; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.botonCalcular.move(50, 280)

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(150)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(self.letra1)
        self.volverMenu.setStyleSheet("background-color: #FF66FF; color: #66FFFF; padding: 10px;")
        self.volverMenu.move(50, 320)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.close()





# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = Addemple1()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())