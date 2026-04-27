from clases.ejercicio1 import Ejercicio1
from PyQt5 import QtWidgets, uic

class VentanaCalculadora1(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/load_ventana_ejercicios.ui", self) 

        self.btnCalcular.clicked.connect(self.ejecutar_ejercicio)

        self.show()

    def ejecutar_ejercicio(self):
        try:
            x = list(map(float, self.inputX.text().split(",")))
            y = list(map(float, self.inputY.text().split(",")))
            xk = float(self.inputXk.text())

            if len(x) != len(y):
                raise ValueError("Datos inválidos")

            ejercicio = Ejercicio1(x, y, xk)
            ejercicio.calcular()

            self.lblB0.setText(f"b0: {ejercicio.b0:.4f}")
            self.lblB1.setText(f"b1: {ejercicio.b1:.4f}")
            self.lblR.setText(f"r: {ejercicio.r:.4f}")
            self.lblYk.setText(f"Predicción: {ejercicio.yk:.4f}")

        except:
            self.lblB0.setText("b0: error")
            self.lblB1.setText("b1: error")
            self.lblR.setText("r: error")
            self.lblYk.setText("Predicción: error")
