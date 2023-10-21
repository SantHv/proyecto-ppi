import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel, QTextEdit, QVBoxLayout, QWidget, QFrame

class Vertareas12(QMainWindow):
    def __init__(self, tareas):
        super(Vertareas12, self).__init__()

        self.setWindowTitle("Tareas Agregadas")
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
        letrero1.setText("Tareas Agregadas")
        letrero1.setFont(fuente)
        letrero1.setStyleSheet("background-color: white; color: #800080; padding: 30px;")
        letrero1.setFixedWidth(350)
        letrero1.move(250, 40)

        # Widget contenedor para las tareas
        self.contenedor_tareas = QWidget(self)
        self.layout_tareas = QVBoxLayout(self.contenedor_tareas)
        self.layout_tareas.setAlignment(Qt.AlignTop)
        self.contenedor_tareas.setGeometry(100, 100, 600, 400)

        # Agregar tareas al contenedor
        for tarea in tareas:
            tarea_widget = self.crear_widget_tarea(tarea)
            self.layout_tareas.addWidget(tarea_widget)

    def crear_widget_tarea(self, tarea):
        # Crear un cuadro para encapsular la tarea
        cuadro_tarea = QFrame(self)
        cuadro_tarea.setFrameShape(QFrame.Box)
        cuadro_tarea.setFrameShadow(QFrame.Plain)
        cuadro_tarea.setStyleSheet("background-color: #F0F0F0; padding: 10px; margin: 10px;")

        layout = QVBoxLayout(cuadro_tarea)
        layout.setAlignment(Qt.AlignTop)

        # Agregar el ID de la tarea
        id_label = QLabel("ID de Tarea: {}".format(tarea["id"]))
        layout.addWidget(id_label)

        # Agregar la especificación de la tarea
        especificacion_label = QLabel("Especificación: {}".format(tarea["especificacion"]))
        layout.addWidget(especificacion_label)

        return cuadro_tarea

if __name__ == '__main__':
    # Ejemplo de lista de tareas (puedes reemplazarlo con tus propios datos)
    tareas = [
        {"id": 1, "especificacion": "Realizar informe"},
        {"id": 2, "especificacion": "Revisar correos electrónicos"},
        {"id": 3, "especificacion": "Preparar presentación"}
    ]

    aplicacion1 = QApplication(sys.argv)
    v1 = Vertareas12(tareas)
    v1.show()
    sys.exit(aplicacion1.exec_())