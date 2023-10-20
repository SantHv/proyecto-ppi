import sys

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFontDatabase, QFont, QPixmap
from PyQt5.QtWidgets import QWidget, QDesktopWidget, QVBoxLayout, QLabel, QLineEdit, QApplication, QPushButton, \
    QMainWindow


class addtarea11(QMainWindow):
    # Hacer el metodo de construccion de la ventana
    def __init__(self):
        super(addtarea11,self).__init__()

        self.setWindowTitle("Agregar Tarea")

        # Poner el color  de fondo a la ventana
        self.setStyleSheet("background-color: #EDEDED;")

        # Estableciendo las propiedades de ancho y alto
        self.ancho = 500
        self.alto = 500

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
        self.letrero1 = QLabel(self)
        # Le escribimos el texto
        self.letrero1.setText("Titulo De la Tarea:")
        # Le asignamos el tipo de letra
        self.letrero1.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.letrero1.setStyleSheet("background-color: white ; color: black; padding: 30px;")
        self.letrero1.setFixedWidth(250)

        self.letrero1.move(0, 20)



        # Hacemos el campo para ingresar el primer numero
        self.titleTask = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.titleTask.setFixedWidth(400)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.titleTask.setMaxLength(100)

        self.titleTask.move(30, 45)

        # Hacemos el letrero
        self.Qlabel1 = QLabel(self)
        # Le escribimos el texto
        self.Qlabel1.setText("Especificaciones:")
        # Le asignamos el tipo de letra
        self.Qlabel1.setFont(self.letra2)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.Qlabel1.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.Qlabel1.setFixedWidth(200)

        self.Qlabel1.move(30, 80)

        # Hacemos el campo para ingresar el primer numero
        self.Qline1 = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.Qline1.setFixedWidth(400)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.Qline1.setMaxLength(300)
        self.Qline1.setFixedHeight(200)


        self.Qline1.move(30, 110)

        # Hacemos un boton para hacer los calculos
        self.botonTarea = QPushButton(self)
        self.botonTarea.setText("Agregar Tarea")
        # Establecemos el ancho del boton
        self.botonTarea.setFixedWidth(400)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.botonTarea.setStyleSheet("background-color: purple; color: black; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.botonTarea.move(30, 380)

        # Hacemos el letrero
        self.Qlabel2 = QLabel(self)
        # Le escribimos el texto
        self.Qlabel2.setText("Agregar ID:")
        # Le asignamos el tipo de letra
        self.Qlabel2.setFont(self.letra1)
        # Le ponemos color de fondo, color de texto y margenes al letrero
        self.Qlabel2.setStyleSheet("background-color: #White; color: #FFFFFF; padding: 40px;")
        self.Qlabel2.setFixedWidth(200)
        self.Qlabel2.move(30,310)

        # Hacemos el campo para ingresar el primer numero
        self.titleTask = QLineEdit(self)
        # Definimos el ancho del campo en 200px
        self.titleTask.setFixedWidth(400)
        # Establecemos que solo se ingrese un numero maximo de 20 digitos
        self.titleTask.setMaxLength(100)

        self.titleTask.move(30, 340)

        # Hacemos un boton para hacer los calculos
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver Menu")
        # Establecemos el ancho del boton
        self.volverMenu.setFixedWidth(400)
        # Le ponemos color de fondo, color de texto y margenes al boton
        self.volverMenu.setStyleSheet("background-color: #FF66FF; color: #66FFFF; padding: 30px;")
        # ponemos el boton de 5 hacia abajo
        self.volverMenu.move(30, 420)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
            self.close()







# Este if de decision se llama si se ejecuta el archivo
if __name__ == '__main__':
    # creamos una aplicacion pyqt5
    aplicacion1 = QApplication(sys.argv)
    # creamos una ventana
    v1 = addtarea11()
    # indicamos que la ventana se deje observar
    v1.show()
    # indicamos que la ventana se deje cerrar

    sys.exit(aplicacion1.exec_())