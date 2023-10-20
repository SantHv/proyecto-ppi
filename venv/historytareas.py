import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit

# Importa tus otras clases
from addTarea import addtarea11
from AddEmpleado import Addemple1
from editTarea import editTarea1

class HistorialTareas(QMainWindow):
    def __init__(self):
        super(HistorialTareas, self).__init__()

        self.setWindowTitle("Historial de Tareas")
        self.setStyleSheet("background-color: #EDEDED;")
        self.ancho = 800
        self.alto = 600
        self.resize(self.ancho, self.alto)

        # Centra la ventana
        pantalla = self.frameGeometry()
        centro = QApplication.desktop().screenGeometry().center()
        pantalla.moveCenter(centro)
        self.move(pantalla.topLeft())

        self.setFixedWidth(self.ancho)
        self.setFixedHeight(self.alto)
        self.setStyleSheet("background-color: White;")

        # Fuente para letreros y botones
        fuente = QFont()
        fuente.setFamily("Arial")
        fuente.setPointSize(18)

        fuente2 = QFont()
        fuente2.setFamily("Arial")
        fuente2.setPointSize(10)

        # Letrero
        letrero1 = QLabel(self)
        letrero1.setText("Historial de Tareas")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("background-color: white; color: #800080; padding: 30px;")
        letrero1.setFixedWidth(400)
        letrero1.move(250, 40)

        # Área de texto para mostrar el historial
        self.textoHistorial = QTextEdit(self)
        self.textoHistorial.setPlaceholderText("Aquí se mostrará el historial de tareas.")
        self.textoHistorial.setReadOnly(True)
        self.textoHistorial.setGeometry(100, 100, 600, 400)

        # Botón para volver al menú principal
        self.volverMenu = QPushButton(self)
        self.volverMenu.setText("Volver al Menú")
        self.volverMenu.setFixedWidth(150)
        self.volverMenu.setFixedHeight(40)
        self.volverMenu.setFont(fuente2)
        self.volverMenu.setStyleSheet("background-color: #FF66FF; color: #66FFFF; padding: 10px;")
        self.volverMenu.move(325, 520)
        self.volverMenu.clicked.connect(self.cerrar_ventana)

    def cerrar_ventana(self):
        self.close()

if __name__ == '__main__':
    aplicacion1 = QApplication(sys.argv)
    v1 = HistorialTareas()
    v1.show()
    sys.exit(aplicacion1.exec_())