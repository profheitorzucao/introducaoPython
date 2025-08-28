from enum import Enum

class Cor(Enum):
    Vermelho = 1
    Verde = 2
    Azul =3


print(Cor.Vermelho.name)
print(Cor.Vermelho.value)

if(Cor.Vermelho.value == 1):
    print("OK")

if(Cor.Verde.value > 0):
    print("OK")