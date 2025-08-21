class Animal:
    def falar(self):
        print("Eu sou um animal")

class Cachorro(Animal):
    def Latir(self):
        print("Auau")
        super().falar()
        
    

meu_cachorro = Cachorro()
meu_cachorro.Latir()