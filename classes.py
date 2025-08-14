class Pessoa:
    nome = None
    Idade = None

    def apresenta(self):
     print(f"Oi, eu sou {self.nome} tenho {self.Idade}")


Heitor = Pessoa()
Heitor.nome = "Heitor"
Heitor.Idade = 35
Heitor.apresenta()

class Animal:
   def __init__(self, especie, familia):
      self.Especie = especie
      self.Familia = familia
   def apresenta(self):
      print(f"A {self.Especie} pertence a familia {self.Familia}")  

cachorro = Animal("canis familiaris", "canidae")
cachorro.apresenta()