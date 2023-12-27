import os
import sys
import json
from Codigos_LeaderBoard.Main_Leaderboard_FV import LeaderBoard
from welcome_window import WelcomeWindow
from PyQt6.QtWidgets import QMessageBox
from name_window import NameWindow
# Importar Lecciones modulo 1
from M1_LESSON_1_Codification.M1_L1_Main import M1_L1_Main as m1l1
from M1_LESSON_2_Working_with_Numerical_Data.M1_L2_Main import M1_L2_Main as m1l2
from M1_LESSON_3_Working_with_Text_Data.M1_L3_Main import M1_L3_Main as m1l3
from M1_LESSON_4_Mixing_things_up.M1_L4_Main import M1_L4_Main as m1l4
from M1_LESSON_5_Labeling_Storing_and_Handling_Data_with_Variables.M1_L5_Main import M1_L5_Main as m1l5
# Importar Lecciones modulo 2
from M2_LESSON_1_Taking_User_Input.M2_L1_Main import M2_L1_Main as m2l1
from M2_LESSON_2_Working_with_Input.M2_L2_Main import M2_L2_Main as m2l2
from M2_LESSON_3_In_Place_Operators.M2_L3_Main import M2_L3_Main as m2l3
# Importar Lecciones modulo 3
from M3_LESSON_1_Booleans_and_Comparisons.M3_L1_Main import M3_L1_Main as m3l1
from M3_LESSON_2_If_Statements.M3_L2_Main import M3_L2_Main as m3l2
from M3_LESSON_3_Else_Statements.M3_L3_Main import M3_L3_Main as m3l3
from M3_LESSON_4_Boolean_Logic.M3_L4_Main import M3_L4_Main as m3l4
from M3_LESSON_5_while_Loops.M3_L5_Main import M3_L5_Main as m3l5
# Importar Lecciones modulo 4
from M4_LESSON_1_Lists.M4_L1_Main import M4_L1_Main as m4l1
from M4_LESSON_2_List_Operations.M4_L2_Main import M4_L2_Main as m4l2
from M4_LESSON_3_For_Loops.M4_L3_Main import M4_L3_Main as m4l3
from M4_LESSON_4_Ranges.M4_L4_Main import M4_L4_Main as m4l4
from M4_LESSON_5_List_Slices.M4_L5_Main import M4_L5_Main as m4l5
# Importar Lecciones modulo 5
from M5_LESSON_1_Functions.M5_L1_Main import M5_L1_Main as m5l1
from M5_LESSON_2_List_Functions.M5_L2_Main import M5_L2_Main as m5l2
from M5_LESSON_3_String_Functions.M5_L3_Main import M5_L3_Main as m5l3
from M5_LESSON_4_Making_Your_Own_Functions.M5_L4_Main import M5_L4_Main as m5l4
from M5_LESSON_5_Function_Arguments.M5_L5_Main import M5_L5_Main as m5l5
from M5_LESSON_6_Returning_From_Functions.M5_L6_Main import M5_L6_Main as m5l6
from M5_LESSON_7_Comments_and_Docstrings.M5_L7_Main import M5_L7_Main as m5l7

from pathlib import Path
from PyQt6.QtWidgets import QApplication
from PyQt6 import QtWidgets, QtCore, QtGui

class UserGuideDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Guía de Usuario")
        self.setWindowIcon(QtGui.QIcon('Icons/guia_usuario_icon.jpeg'))  # Establece el ícono de la ventana
        self.setGeometry(100, 100, 800, 600)

        layout = QtWidgets.QVBoxLayout(self)
        label = QtWidgets.QLabel("Sistema de puntos:\nCompletar una página = 1 punto\nResponder respuesta correctamente al primer intento = 2 puntos\nResponder respuesta correctamente al segundo o más intentos = 1 punto\nFinalizar una lessión = 5 puntos")
        label.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(label)


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        # Carga de estilos y configuración inicial de la ventana
        # Módulo 1
        self.m1_lesson1_window = None
        self.m1_lesson2_window = None
        self.m1_lesson3_window = None
        self.m1_lesson4_window = None
        self.m1_lesson5_window = None

        # Módulo 2
        self.m2_lesson1_window = None
        self.m2_lesson2_window = None
        self.m2_lesson3_window = None

        # Módulo 3
        self.m3_lesson1_window = None
        self.m3_lesson2_window = None
        self.m3_lesson3_window = None
        self.m3_lesson4_window = None
        self.m3_lesson5_window = None

        # Módulo 4
        self.m4_lesson1_window = None
        self.m4_lesson2_window = None
        self.m4_lesson3_window = None
        self.m4_lesson4_window = None
        self.m4_lesson5_window = None

        # Módulo 5
        self.m5_lesson1_window = None
        self.m5_lesson2_window = None
        self.m5_lesson3_window = None
        self.m5_lesson4_window = None
        self.m5_lesson5_window = None
        self.m5_lesson6_window = None
        self.m5_lesson7_window = None

        self.estado_lecciones = {}

        self.usuario_actual = self.load_current_user()  # Carga el usuario actual
        self.progreso_usuario = self.load_user_progress(self.usuario_actual)  # Carga el progreso del usuario
        self.actualizar_lecciones(self.progreso_usuario)

        self.styles = self.load_styles("styles.json")
        self.setWindowTitle("Menú - Principal")
        self.setGeometry(100, 100, 800, 600)
        self.setStyleSheet(f"background-color: {self.styles['main_background_color']};")

        # Configura la hoja de estilos para los menús aquí
        self.setStyleSheet("""
                    QMenu {
                        background-color: #87CEEB; /* Color de fondo de tu menú */
                        border: none;
                    }
                    QMenu::item {
                        padding: 5px 25px 5px 20px; /* Ajusta el espaciado como prefieras */
                        background-color: transparent;
                    }
                    QMenu::item:selected { /* Cuando pasas el ratón por encima */
                        background-color: #ADD8E6; /* Color de fondo al pasar el ratón por encima */
                        color: black; /* Cambia esto al color de texto deseado */
                    }
                """)

        # Configuración del widget central y layout principal
        central_widget = QtWidgets.QWidget()
        self.setCentralWidget(central_widget)
        layout = QtWidgets.QVBoxLayout(central_widget)

        # Creación y configuración del título
        title = QtWidgets.QLabel("Menú - Modulos")
        title.setStyleSheet(
            f"background-color: {self.styles['title_background_color']};"
            f"border: 1px solid {self.styles['title_border_color']};"
            f"color: {self.styles['title_text_color']};"
            f"font-size: {self.styles['font_size_titles']}px;")
        title.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        title.setFixedHeight(50)
        layout.addWidget(title)

        # Configuración del layout para botones
        button_layout = QtWidgets.QHBoxLayout()
        button_reset_layout = QtWidgets.QVBoxLayout()

        # Botón Leaderboard
        leaderboard_btn = QtWidgets.QPushButton("Leaderboard")
        leaderboard_btn.setStyleSheet(f"background-color: {self.styles['submit_button_color']}; font-size: {self.styles['font_size_buttons']}px;")
        leaderboard_btn.clicked.connect(self.abrir_leaderboard)
        leaderboard_btn.setIcon(QtGui.QIcon('Icons/leaderboard_icon.png'))
        button_layout.addWidget(leaderboard_btn)

        # Botón Guía de usuarios
        guia_usuario_btn = QtWidgets.QPushButton("Guía de usuarios")
        guia_usuario_btn.setStyleSheet(f"background-color: {self.styles['submit_button_color']}; font-size: {self.styles['font_size_buttons']}px;")
        guia_usuario_btn.clicked.connect(self.abrir_guia_usuario)
        guia_usuario_btn.setIcon(QtGui.QIcon('Icons/guia_usuario_icon.jpeg'))
        button_layout.addWidget(guia_usuario_btn)

        # Crear el botón de reinicio
        reinicio_btn = QtWidgets.QPushButton("Reiniciar")
        reinicio_btn.setStyleSheet("background-color: red; color: white;")  # Estilo del botón
        reinicio_btn.clicked.connect(self.reiniciar_aplicacion)  # Conectar el botón a la función de reinicio
        button_reset_layout.addWidget(reinicio_btn)

        modulos_btn = self.setup_modulos_menu()
        button_layout.addWidget(modulos_btn)  # Añade modulos_btn al button_layout

        layout.addLayout(button_layout)
        layout.addLayout(button_reset_layout)

    def reiniciar_aplicacion(self):
        self.close()  # Cierra la ventana actual
        self.new_instance = MainWindow()  # Crea una nueva instancia de MainWindow
        self.new_instance.showMaximized()

    def recargar_progreso_usuario(self):
        try:
            # Cargar el progreso del usuario actualizado desde el archivo
            with open('progreso.json', 'r', encoding='UTF-8') as file:
                progreso = json.load(file)
            self.progreso_usuario = progreso.get(self.usuario_actual, {})

            # Actualizar el estado de las lecciones en la interfaz de usuario
            self.actualizar_lecciones(self.progreso_usuario)
        except Exception as e:
            print(f"Error al recargar el progreso del usuario: {e}")

    def load_current_user(self):
        try:
            with open('current_user.json', 'r', encoding='UTF-8') as file:
                user_data = json.load(file)
            return user_data.get("current_user")
        except FileNotFoundError:
            print("Archivo current_user.json no encontrado.")
            return None

    def load_user_progress(self, username):
        try:
            with open('progreso.json', 'r', encoding='UTF-8') as file:
                progreso = json.load(file)
            return progreso.get(username, {})
        except FileNotFoundError:
            print("Archivo progreso.json no encontrado.")
            return {}

    def actualizar_lecciones(self, estado_usuario):

        # Modulo 1
        self.estado_lecciones = {
            "Modulo1": {
                "Leccion1": estado_usuario.get("Modulo1", {}).get("Leccion1", False),
                "Leccion2": estado_usuario.get("Modulo1", {}).get("Leccion2", False),
                "Leccion3": estado_usuario.get("Modulo1", {}).get("Leccion3", False),
                "Leccion4": estado_usuario.get("Modulo1", {}).get("Leccion4", False),
                "Leccion5": estado_usuario.get("Modulo1", {}).get("Leccion5", False),
            },
            "Modulo2": {
                "Leccion1": estado_usuario.get("Modulo2", {}).get("Leccion1", False),
                "Leccion2": estado_usuario.get("Modulo2", {}).get("Leccion2", False),
                "Leccion3": estado_usuario.get("Modulo2", {}).get("Leccion3", False),
            },
            "Modulo3": {
                "Leccion1": estado_usuario.get("Modulo3", {}).get("Leccion1", False),
                "Leccion2": estado_usuario.get("Modulo3", {}).get("Leccion2", False),
                "Leccion3": estado_usuario.get("Modulo3", {}).get("Leccion3", False),
                "Leccion4": estado_usuario.get("Modulo3", {}).get("Leccion4", False),
                "Leccion5": estado_usuario.get("Modulo3", {}).get("Leccion5", False),
            },
            "Modulo4": {
                "Leccion1": estado_usuario.get("Modulo4", {}).get("Leccion1", False),
                "Leccion2": estado_usuario.get("Modulo4", {}).get("Leccion2", False),
                "Leccion3": estado_usuario.get("Modulo4", {}).get("Leccion3", False),
                "Leccion4": estado_usuario.get("Modulo4", {}).get("Leccion4", False),
                "Leccion5": estado_usuario.get("Modulo4", {}).get("Leccion5", False),
            },
            "Modulo5": {
                "Leccion1": estado_usuario.get("Modulo5", {}).get("Leccion1", False),
                "Leccion2": estado_usuario.get("Modulo5", {}).get("Leccion2", False),
                "Leccion3": estado_usuario.get("Modulo5", {}).get("Leccion3", False),
                "Leccion4": estado_usuario.get("Modulo5", {}).get("Leccion4", False),
                "Leccion5": estado_usuario.get("Modulo5", {}).get("Leccion5", False),
                "Leccion6": estado_usuario.get("Modulo5", {}).get("Leccion6", False),
                "Leccion7": estado_usuario.get("Modulo5", {}).get("Leccion7", False)
            }
        }

    def añadir_submenu(self, nombre_modulo, numero_lecciones, menu_principal):
        submenu = QtWidgets.QMenu(nombre_modulo, self)

        # Añade acciones y conecta con funciones específicas para cada lección
        for leccion_numero in range(1, numero_lecciones + 1):
            accion_leccion = submenu.addAction(f"Lección {leccion_numero}")
            accion_leccion.triggered.connect(lambda _, n=leccion_numero, m=nombre_modulo: self.abrir_leccion(m, n))

        menu_principal.addMenu(submenu)

    def abrir_leccion(self, nombre_modulo, numero_leccion):
        nombre_modulo_key = nombre_modulo.replace(" ", "")
        try:
            if self.estado_lecciones[nombre_modulo_key]["Leccion" + str(numero_leccion)]:
                if nombre_modulo == "Modulo 1":
                    if numero_leccion == 1:
                        if not self.m1_lesson1_window:
                            self.m1_lesson1_window = m1l1()
                        self.m1_lesson1_window.showMaximized()

                    elif numero_leccion == 2:
                        if not self.m1_lesson2_window:
                            self.m1_lesson2_window = m1l2()
                        self.m1_lesson2_window.showMaximized()

                    elif numero_leccion == 3:
                        if not self.m1_lesson3_window:
                            self.m1_lesson3_window = m1l3()
                        self.m1_lesson3_window.showMaximized()

                    elif numero_leccion == 4:
                        if not self.m1_lesson4_window:
                            self.m1_lesson4_window = m1l4()
                        self.m1_lesson4_window.showMaximized()

                    elif numero_leccion == 5:
                        if not self.m1_lesson5_window:
                            self.m1_lesson5_window = m1l5()
                        self.m1_lesson5_window.showMaximized()

                elif nombre_modulo == "Modulo 2":
                    if numero_leccion == 1:
                        if not self.m2_lesson1_window:
                            self.m2_lesson1_window = m2l1()
                        self.m2_lesson1_window.showMaximized()

                    if numero_leccion == 2:
                        if not self.m2_lesson2_window:
                            self.m2_lesson2_window = m2l2()
                        self.m2_lesson2_window.showMaximized()

                    if numero_leccion == 3:
                        if not self.m2_lesson3_window:
                            self.m2_lesson3_window = m2l3()
                        self.m2_lesson3_window.showMaximized()

                elif nombre_modulo == "Modulo 3":
                    if numero_leccion == 1:
                        if not self.m3_lesson1_window:
                            self.m3_lesson1_window = m3l1()
                        self.m3_lesson1_window.showMaximized()

                    if numero_leccion == 2:
                        if not self.m3_lesson2_window:
                            self.m3_lesson2_window = m3l2()
                        self.m3_lesson2_window.showMaximized()

                    if numero_leccion == 3:
                        if not self.m3_lesson3_window:
                            self.m3_lesson3_window = m3l3()
                        self.m3_lesson3_window.showMaximized()

                    if numero_leccion == 4:
                        if not self.m3_lesson4_window:
                            self.m3_lesson4_window = m3l4()
                        self.m3_lesson4_window.showMaximized()

                    if numero_leccion == 5:
                        if not self.m3_lesson5_window:
                            self.m3_lesson5_window = m3l5()
                        self.m3_lesson5_window.showMaximized()

                elif nombre_modulo == "Modulo 4":
                    if numero_leccion == 1:
                        if not self.m4_lesson1_window:
                            self.m4_lesson1_window = m4l1()
                        self.m4_lesson1_window.showMaximized()

                    if numero_leccion == 2:
                        if not self.m4_lesson2_window:
                            self.m4_lesson2_window = m4l2()
                        self.m4_lesson2_window.showMaximized()

                    if numero_leccion == 3:
                        if not self.m4_lesson3_window:
                            self.m4_lesson3_window = m4l3()
                        self.m4_lesson3_window.showMaximized()

                    if numero_leccion == 4:
                        if not self.m4_lesson4_window:
                            self.m4_lesson4_window = m4l4()
                        self.m4_lesson4_window.showMaximized()

                    if numero_leccion == 5:
                        if not self.m4_lesson5_window:
                            self.m4_lesson5_window = m4l5()
                        self.m4_lesson5_window.showMaximized()

                elif nombre_modulo == "Modulo 5":
                    if numero_leccion == 1:
                        if not self.m5_lesson1_window:
                            self.m5_lesson1_window = m5l1()
                        self.m5_lesson1_window.showMaximized()

                    if numero_leccion == 2:
                        if not self.m5_lesson2_window:
                            self.m5_lesson2_window = m5l2()
                        self.m5_lesson2_window.showMaximized()

                    if numero_leccion == 3:
                        if not self.m5_lesson3_window:
                            self.m5_lesson3_window = m5l3()
                        self.m5_lesson3_window.showMaximized()

                    if numero_leccion == 4:
                        if not self.m5_lesson4_window:
                            self.m5_lesson4_window = m5l4()
                        self.m5_lesson4_window.showMaximized()

                    if numero_leccion == 5:
                        if not self.m5_lesson5_window:
                            self.m5_lesson5_window = m5l5()
                        self.m5_lesson5_window.showMaximized()

                    if numero_leccion == 6:
                        if not self.m5_lesson6_window:
                            self.m5_lesson6_window = m5l6()
                        self.m5_lesson6_window.showMaximized()

                    if numero_leccion == 7:
                        if not self.m5_lesson7_window:
                            self.m5_lesson7_window = m5l7()
                        self.m5_lesson7_window.showMaximized()
            else:
                self.mostrar_mensaje_bloqueado(nombre_modulo, numero_leccion)
        except Exception as e:
            print(f"Error al abrir {nombre_modulo} - Lección {numero_leccion}: {e}")

    def mostrar_mensaje_bloqueado(self, nombre_modulo, numero_leccion):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Warning)
        msg.setWindowTitle("Lección Bloqueada")
        msg.setText(f"Lo siento, el {nombre_modulo}, Lección {numero_leccion}, está bloqueado.")
        msg.exec()

    def setup_modulos_menu(self):
        modulos_btn = QtWidgets.QToolButton()
        modulos_btn.setText("Modulos")
        modulos_btn.setStyleSheet(f"background-color: {self.styles['submit_button_color']}; font-size: {self.styles['font_size_buttons']}px;")

        modulos_menu = QtWidgets.QMenu()

        # Añadir submenús para cada módulo
        # Dentro de setup_modulos_menu o donde configures los submenús
        self.añadir_submenu("Modulo 1", 5, modulos_menu)
        self.añadir_submenu("Modulo 2", 3, modulos_menu)
        self.añadir_submenu("Modulo 3", 5, modulos_menu)
        self.añadir_submenu("Modulo 4", 5, modulos_menu)
        self.añadir_submenu("Modulo 5", 7, modulos_menu)

        modulos_btn.setMenu(modulos_menu)
        modulos_btn.setPopupMode(QtWidgets.QToolButton.ToolButtonPopupMode.InstantPopup)

        return modulos_btn  # Retorna el botón configurado

    def load_styles(self, file):
        with open(file, 'r') as json_file:
            data = json.load(json_file)
        return data

    def abrir_guia_usuario(self):
        dialog = UserGuideDialog(self)
        dialog.exec()

    def abrir_leaderboard(self):
        LeaderBoard()


def open_main_window():
    mainWin = MainWindow()
    mainWin.showMaximized()
    sys.exit(app.exec())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    intro_pages = WelcomeWindow()
    intro_pages.showMaximized()
    app.exec()
    open_main_window()