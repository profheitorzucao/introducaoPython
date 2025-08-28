class Animal:
    def EmitirSom(self):
        pass

class Cachorro(Animal):
    def EmitirSom(self):
        return "Au Au"
    
class Gato(Animal):
    def EmitirSom(self):
      return "Miau"


def ReproduzirSom(animal: Animal):
    print(animal.EmitirSom())


cachorro1 = Cachorro()
gato1 = Gato()

ReproduzirSom(cachorro1)
ReproduzirSom(gato1)