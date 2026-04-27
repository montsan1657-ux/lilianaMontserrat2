import math
from clases.ejercicio2 import Calculadora

class CalculadoraInversa(Calculadora):
    def __init__(self, p, dof):
        super().__init__(0, dof)
        self.p = p

    def encontrar_x(self):
        x = 1.0
        d = 0.5
        error_permitido = 0.00001

        pasos = []

        self.x = x
        self.integrar()
        p_calculado = self.resultado

        error_anterior = self.p - p_calculado

        while True:
            self.x = x
            self.integrar()
            p_calculado = self.resultado

            error = self.p - p_calculado

            pasos.append(f"x={x:.5f}, pCalc={p_calculado:.5f}, error={error:.5f}, d={d}")

            if abs(error) < error_permitido:
                return x, pasos

            if error_anterior * error < 0:
                d = d / 2

            if p_calculado < self.p:
                x += d
            else:
                x -= d

            error_anterior = error