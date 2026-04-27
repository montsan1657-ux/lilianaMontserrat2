from psp.psp1 import RegresionLineal

class Ejercicio1(object):
    def __init__(self, x, y, xk):
        self.x = x
        self.y = y
        self.xk = xk

        self.b0 = 0
        self.b1 = 0
        self.r = 0
        self.yk = 0

    def calcular(self):
        modelo = RegresionLineal(self.x, self.y)

        self.b1 = modelo.calcular_b1()
        self.b0 = modelo.calcular_b0(self.b1)
        self.r = modelo.correlacion()
        self.yk = modelo.prediccion(self.xk, self.b0, self.b1)