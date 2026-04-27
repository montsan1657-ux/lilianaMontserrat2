import math
from psp.psp1 import RegresionLineal
from clases.ejercicio2 import Calculadora
from clases.ejercicio3 import CalculadoraInversa

class Ejercicio4(object):
    def __init__(self, x, y, xk):
        self.x = x
        self.y = y
        self.xk = xk

        self.b0 = 0
        self.b1 = 0
        self.r = 0
        self.yk = 0

        self.t = 0
        self.p = 0
        self.tail = 0
        self.t_critico = 0
        self.sigma = 0
        self.rango = 0
        self.upi = 0
        self.lpi = 0

    def calcular(self):
        n = len(self.x)

        modelo = RegresionLineal(self.x, self.y)
        self.b1 = modelo.calcular_b1()
        self.b0 = modelo.calcular_b0(self.b1)
        self.r = modelo.correlacion()
        self.yk = modelo.prediccion(self.xk, self.b0, self.b1)

        self.t = abs(self.r) * math.sqrt(n - 2) / math.sqrt(1 - self.r**2)

        calc = Calculadora(self.t, n - 2)
        calc.integrar()
        self.p = calc.resultado

        self.tail = 1 - (2 * self.p)

        inversa = CalculadoraInversa(self.p, n - 2)
        self.t_critico = inversa.encontrar_x()

        suma = 0
        for i in range(n):
            suma += (self.y[i] - self.b0 - self.b1 * self.x[i])**2

        self.sigma = math.sqrt(suma / (n - 2))

        x_avg = sum(self.x) / n

        sum_x = 0
        for i in range(n):
            sum_x += (self.x[i] - x_avg)**2

        self.rango = self.t_critico * self.sigma * math.sqrt(
            1 + (1/n) + ((self.xk - x_avg)**2 / sum_x)
        )

        self.upi = self.yk + self.rango
        self.lpi = self.yk - self.rango