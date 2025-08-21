class Motor:
    def __init__(self, potencia):
        self.Potencia = potencia

class Carro:
    def __init__(self, modelo, potencia_motor):
        self.Modelo = modelo
        self.Motor = Motor(potencia_motor)
    def Detalhes(self):
        print(f"Carro: {self.Modelo}, motor: {self.Motor.Potencia} cv")

carro = Carro("Fusca", "100")
carro.Detalhes()


        
        