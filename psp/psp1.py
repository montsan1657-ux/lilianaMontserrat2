class RegresionLineal(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.n = len(x)

    def promedio(self, lista):
        return sum(lista) / len(lista)

    def calcular_b1(self):
        x_avg = self.promedio(self.x)
        y_avg = self.promedio(self.y)

        num = sum((self.x[i] - x_avg) * (self.y[i] - y_avg) for i in range(self.n))
        den = sum((self.x[i] - x_avg) ** 2 for i in range(self.n))

        return num / den

    def calcular_b0(self, b1):
        x_avg = self.promedio(self.x)
        y_avg = self.promedio(self.y)

        return y_avg - b1 * x_avg

    def correlacion(self):
        suma_xy = sum(self.x[i] * self.y[i] for i in range(self.n))
        suma_x = sum(self.x)
        suma_y = sum(self.y)
        suma_x2 = sum(x**2 for x in self.x)
        suma_y2 = sum(y**2 for y in self.y)

        num = (self.n * suma_xy) - (suma_x * suma_y)
        den = ((self.n * suma_x2 - suma_x**2) * (self.n * suma_y2 - suma_y**2)) ** 0.5

        return num / den

    def prediccion(self, xk, b0, b1):
        return b0 + b1 * xk