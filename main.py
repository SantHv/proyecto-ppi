import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow, QMessageBox, QCheckBox
from ventana2 import Login2
from ventana3 import Login3
from registrar import registrar1

class Login5(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(Login5,self).__init__()


        self.setWindowTitle("Login de usuario")

        # Poner el color  de fondo a la ventana
        self.setStyleSheet("background-color: #EDEDED;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 800
        self.alto = 600

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
        self.letra1.setPointSize(18)

        # Hacemos el tipo de letra
        self.letra2 = QFont()
        # Le asignamos el tipo de letra descargado
        self.letra2.setFamily("Arial")
        # Le asignamos el tamaño
        self.letra2.setPointSize(16)

        # Hacemos el letrero
        self.letrero1 = QLabel(self)
        # Le escribimos el texto
        self.letrero1.setText("Domestic Space")
        # Le asignamos el tipo de letra
        self.letrero1.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color: white ; color: #800080; padding: 50px;")
        self.letrero1.setFixedWidth(500)

        self.letrero1.move(250, 40)

        # Hacemos el letrero
        self.login = QLabel(self)
        # Le escribimos el texto
        self.login.setText("Usuario")
        # Le asignamos el tipo de letra
        self.login.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.login.setStyleSheet("background-color: #White; color: #0000FF; padding: 40px;")
        self.login.setFixedWidth(250)
        self.login.move(300,100)






        # Hacemos el campo para ingresar el primer numero
        self.editLogin = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editLogin.setFixedWidth(250)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editLogin.setMaxLength(20)

        self.editLogin.move(305, 160)

        # Hacemos el letrero
        self.contraseña = QLabel(self)
        # Le escribimos el texto
        self.contraseña.setText("Contraseña")
        # Le asignamos el tipo de letra
        self.contraseña.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.contraseña.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.contraseña.setFixedWidth(200)

        self.contraseña.move(305, 200)

        # Hacemos el campo para ingresar el primer numero
        self.editContraseña = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.editContraseña.setFixedWidth(250)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.editContraseña.setMaxLength(20)
        self.editContraseña.setEchoMode(QLineEdit.Password)
        self.editContraseña.move(305, 240)

        self.botonCalcular = QPushButton(self)
        self.botonCalcular.setText("Iniciar Sesión")
        self.botonCalcular.setFixedWidth(200)
        self.botonCalcular.setStyleSheet("background-color: #FF66FF; color: #000000  ; padding: 30px;")
        self.botonCalcular.move(325, 300)
        self.botonCalcular.setFixedHeight(40)

        self.botonRegistrar = QPushButton(self)
        self.botonRegistrar.setText("Registrarse")
        self.botonRegistrar.setFixedWidth(200)
        self.botonRegistrar.setStyleSheet("background-color: #FF66FF; color: #000000  ; padding: 30px;")
        self.botonRegistrar.move(325, 360)
        self.botonRegistrar.setFixedHeight(40)

        # Create a checkbox for toggling password visibility
        self.mostrar_contraseña_checkbox = QCheckBox("Mostrar Contraseña", self)
        self.mostrar_contraseña_checkbox.move(570, 240)
        self.mostrar_contraseña_checkbox.setFixedWidth(200)
        self.mostrar_contraseña_checkbox.stateChanged.connect(self.toggle_password_visibility)


        # Conectamos el botón a la función que verifica las credenciales
        self.botonCalcular.clicked.connect(self.check_login)

        # Conectamos el botón a la función que verifica las credenciales
        self.botonRegistrar.clicked.connect(self.abrir_registrar)
    def abrir_registrar(self):
        self.boton_Registrar = registrar1()
        self.boton_Registrar.show()

    def check_login(self):
        # Obtenemos el nombre de usuario y contraseña ingresados
        username = self.editLogin.text()
        password = self.editContraseña.text()

        # Aquí debes implementar la lógica para verificar las credenciales.
        if username == 'empleador' and password == 'prueba12345':
            QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso.')

            # Abre la ventana Ventana2
            self.abrir_ventana2()
        elif username == 'empleado' and password == 'prueba12345':
            QMessageBox.information(self, 'Éxito', 'Inicio de sesión exitoso.')

            # Abre la ventana Ventana2
            self.abrir_ventana33()
        else:
            QMessageBox.warning(self, 'Error', 'Credenciales incorrectas.')

    def abrir_ventana2(self):
            self.ventana2 = Login2()
            self.ventana2.show()
            self.hide()

    def abrir_ventana33(self):
            self.ventana33 = Login3()
            self.ventana33.show()
            self.hide()
    def toggle_password_visibility(self, state):
        if state == Qt.Checked:
            self.editContraseña.setEchoMode(QLineEdit.Normal)
        else:
            self.editContraseña.setEchoMode(QLineEdit.Password)









# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = Login5()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())