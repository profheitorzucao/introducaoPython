from abc import ABC, abstractmethod

class Ligavel(ABC):
    @abstractmethod
    def Ligar(self):
        pass

class Desligavel(ABC):
    @abstractmethod
    def Desligar(self):
        pass

class Carregavel(ABC):
    @abstractmethod
    def Carregar(self):
        pass
    def Carregado(self):
        print("SmartPhone Carregado")

class SmartPhone(Ligavel, Desligavel, Carregavel):
    def Ligar(self):
        print("SmartPhone ligado")
    def Desligar(self):
        print("SmartPhone desligado")
    def Carregar(self):
        print("SmartPhone Carregando")


iphone = SmartPhone()

iphone.Ligar()
iphone.Desligar()
iphone.Carregar()
iphone.Carregado()