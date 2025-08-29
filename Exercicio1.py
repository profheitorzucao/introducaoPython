import math
class Forma:
    def calcular_area():
        pass

class Quadrado(Forma):
    def calcular_area(self, lado):
        return lado * lado

class Circulo(Forma):
    def calcular_area(self, raio):
        return format(math.pi * (raio * raio), '.2f')
    

class Retangulo(Forma):
    def calcular_area(self, base, altura):
        return base * altura
        
    

quadrado = Quadrado()
print(quadrado.calcular_area(2))

circulo = Circulo()
print(circulo.calcular_area(3))

retangulo = Retangulo()
print(retangulo.calcular_area(2,7))
        
        