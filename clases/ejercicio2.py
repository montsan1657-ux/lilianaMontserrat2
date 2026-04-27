import math

class Calculadora(object):
    def __init__(self, x, dof):
        self.x = x
        self.dof = dof
        self.resultado = 0

    def tDistribution(self, x):
        num = math.gamma((self.dof + 1) / 2)
        den = math.sqrt(self.dof * math.pi) * math.gamma(self.dof / 2)
        return (num / den) * (1 + (x**2)/self.dof) ** (-(self.dof + 1) / 2)

    def simpson(self, numSeg):
        W = self.x / numSeg
        suma = self.tDistribution(0) + self.tDistribution(self.x)

        for i in range(1, numSeg):
            xi = i * W

            if i % 2 == 0:
                suma += 2 * self.tDistribution(xi)
            else:
                suma += 4 * self.tDistribution(xi)

        return (W / 3) * suma

    def integrar(self):
        numSeg = 10
        E = 0.00001

        old = self.simpson(numSeg)

        while True:
            numSeg *= 2
            new = self.simpson(numSeg)

            if abs(new - old) < E:
                self.resultado = new
                return

            old = new