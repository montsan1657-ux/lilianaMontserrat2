from PyQt5 import QtWidgets, uic
from clases.ejercicio2 import Calculadora
from clases.ejercicio3 import CalculadoraInversa

class VentanaCalculadora3(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        uic.loadUi("gui/simson_inverso.ui", self)
        self.show()
        
        self.pushButton.clicked.connect(self.calcular)

    def calcular(self):
        try:
            valor = float(self.edit_numero1.text())
            dof = int(self.edit_numero2.text())

            # 🔥 CASO INVERSO (el que estás trabajando)
            if valor < 1:
                calc = CalculadoraInversa(valor, dof)
                x, pasos = calc.encontrar_x()

                iteraciones = ""
                errores = ""
                ds = ""

                for i, paso in enumerate(pasos):
                    iteraciones += f"Iter {i+1}\n"

                    partes = paso.split(", ")
                    # ["x=...", "pCalc=...", "error=...", "d=..."]

                    errores += partes[2] + "\n"
                    ds += partes[3] + "\n"

                # 🔹 mostrar en labels
                self.label_resultado.setText(f"x:\n{x}")
                self.label_resultado2.setText(iteraciones)
                self.label_resultado3.setText(errores)
                self.label_resultado4.setText(ds)

            # 🔥 CASO NORMAL
            else:
                calc = Calculadora(valor, dof)
                calc.integrar()

                self.label_resultado.setText(f"p:\n{calc.resultado}")
                self.label_resultado2.setText("")
                self.label_resultado3.setText("")
                self.label_resultado4.setText("")

        except:
            self.label_resultado.setText("Error en datos")
            self.label_resultado2.setText("")
            self.label_resultado3.setText("")
            self.label_resultado4.setText("")