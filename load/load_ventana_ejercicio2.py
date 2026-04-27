from PyQt5 import QtWidgets, uic
from clases.ejercicio2 import Calculadora

class VentanaCalculadora(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/simpson.ui", self)
        self.show()
        
        self.boton_sumar.clicked.connect(self.calcular)

    def calcular(self):
        try:
            x = float(self.edit_numero1.text())
            dof = int(self.edit_numero2.text())

            calc = Calculadora(x, dof)
            calc.integrar()

            self.label_resultado.setText(str(calc.resultado))

        except:
            self.label_resultado.setText("Error en datos")