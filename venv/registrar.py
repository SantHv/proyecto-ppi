import sys

from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QPushButton, QLineEdit, QMainWindow, QDesktopWidget, QLabel, QApplication


class registrar1(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(registrar1,self).__init__()

        self.setWindowTitle("Registro")

        # Poner el color  de fondo a la ventana
        self.setStyleSheet("background-color: #C5F9E8;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 600
        self.alto = 800

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



        # Hacemos el tipo de letra
        self.letra1 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra1.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra1.setPointSize(18)

        self.letra3 = QFont()
        self.letra3.setFamily("Arial")
        self.letra3.setPointSize(12)
        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(12)

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        # Le escribimos el texto
        self.letrero1.setText("Registro")
        # Le asignamos el tipo de letra
        self.letrero1.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color:#C5F9E8  ; color: #000000; padding: 40px;")
        self.letrero1.setFixedWidth(400)
        self.letrero1.setFixedHeight(40)

        self.letrero1.move(20, 40)

        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Usuario")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(200)

        self.login.move(67, 120)

        # Hacemos el campo para ingresar el primer numero
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(200)
        self.editLogin.setStyleSheet("background-color: White")
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editLogin.setMaxLength(20)

        self.editLogin.move(67, 160)

        # Hacemos el letrero
        self.contraseña = QLabel(self)
        # Le escribimos el texto
        self.contraseña.setText("Contraseña")
        # Le asignamos el tipo de letra
        self.contraseña.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.contraseña.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.contraseña.setFixedWidth(200)

        self.contraseña.move(67, 200)

        # Hacemos el campo para ingresar el primer numero
        self.editContraseña = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editContraseña.setFixedWidth(200)
        self.editContraseña.setStyleSheet("background-color: White")
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editContraseña.setMaxLength(20)

        self.editContraseña.move(67, 240)


        # Hacemos el letrero
        self.hotmail = QLabel(self)
        # Le escribimos el texto
        self.hotmail.setText("Correo")
        # Le asignamos el tipo de letra
        self.hotmail.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.hotmail.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.hotmail.setFixedWidth(200)

        self.hotmail.move(67, 280)

        # Hacemos el campo para ingresar el primer numero
        self.lineHotmail = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.lineHotmail.setStyleSheet("background-color: White")
        self.lineHotmail.setFixedWidth(200)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.lineHotmail.setMaxLength(20)

        self.lineHotmail.move(67, 320)

        # Hacemos el letrero
        self.nombre = QLabel(self)
        # Le escribimos el texto
        self.nombre.setText("Nombre")
        # Le asignamos el tipo de letra
        self.nombre.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.nombre.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.nombre.setFixedWidth(200)

        self.nombre.move(67, 360)

        # Hacemos el campo para ingresar el primer numero
        self.lineNombre = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.lineNombre.setFixedWidth(200)
        self.lineNombre.setStyleSheet("background-color: White")
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.lineNombre.setMaxLength(20)

        self.lineNombre.move(67, 400)

        self.botonCalcular = QPushButton(self)
        self.botonCalcular.setText("registrarse")
        self.botonCalcular.setFont(self.letra3)
        self.botonCalcular.setFixedWidth(250)
        self.botonCalcular.setFixedHeight(40)
        self.botonCalcular.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        self.botonCalcular.move(320, 500)



        # Hacemos un boton para hacer los calculos
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver Menu")
        self.volverMenu.setFont(self.letra3)
        # Establecemos el ancho del boton
        self.volverMenu.setFixedWidth(250)
        self.volverMenu.setFixedHeight(40)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.volverMenu.setStyleSheet("background-color: #50D4FA; color: #000000  ; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.volverMenu.move(50, 500)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.close()

# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = registrar1()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())