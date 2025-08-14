class Celular:
    def __init__(self, marca, modelo, memoria):
        self.Marca = marca
        self.Modelo = modelo
        self.Memoria = memoria
    
    def Apresentar(self):
        print(f"Marca: {self.Marca}")
        print(f"Modelo: {self.Modelo}")
        print(f"Memoria: {self.Memoria} GB")
        
galaxy = Celular("Samsung", "M52", "6")
galaxy.Apresentar()