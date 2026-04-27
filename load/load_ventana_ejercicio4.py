from clases.ejercicio4 import Ejercicio4
from PyQt5 import QtWidgets, uic

class VentanaCalculadora4(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/ejercicio4.ui", self)

        self.btnCalcular.clicked.connect(self.ejecutar_ejercicio)

        self.show()

    def ejecutar_ejercicio(self):
        try:
            x = list(map(float, self.inputX.text().split(",")))
            y = list(map(float, self.inputY.text().split(",")))
            xk = float(self.inputXk.text())

            if len(x) != len(y):
                raise ValueError("Datos inválidos")

            ejercicio = Ejercicio4(x, y, xk)
            ejercicio.calcular()

            self.lblB0.setText(f"b0: {ejercicio.b0:.4f}")
            self.lblB1.setText(f"b1: {ejercicio.b1:.4f}")
            self.lblR.setText(f"r: {ejercicio.r:.4f}")
            self.lblYk.setText(f"Predicción: {ejercicio.yk:.4f}")

            self.lblT.setText(f"t: {ejercicio.t:.4f}")
            self.lblP.setText(f"p: {ejercicio.p:.4f}")
            self.lblTail.setText(f"tail: {ejercicio.tail:.4f}")
            self.lblTCritico.setText(f"t crítico: {ejercicio.t_critico:.4f}")

            self.lblRango.setText(f"rango: {ejercicio.rango:.4f}")
            self.lblUPI.setText(f"UPI: {ejercicio.upi:.4f}")
            self.lblLPI.setText(f"LPI: {ejercicio.lpi:.4f}")

        except:
            self.lblB0.setText("b0: error")
            self.lblB1.setText("b1: error")
            self.lblR.setText("r: error")
            self.lblYk.setText("Predicción: error")

            self.lblT.setText("t: error")
            self.lblP.setText("p: error")
            self.lblTail.setText("tail: error")
            self.lblTCritico.setText("t crítico: error")

            self.lblRango.setText("rango: error")
            self.lblUPI.setText("UPI: error")
            self.lblLPI.setText("LPI: error")