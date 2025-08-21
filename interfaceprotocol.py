from typing import Protocol

class Animal(Protocol):
    def falar(self) -> str:
        pass

class Cachorro:
    def falar(self) -> str:
        return "Au au!"

class Gato:
    def falar(self) -> str:
        return "Miau!"
    
class Cavalo:
    def falar(self) -> str:
        return "hiiin in in"


def fazer_barulho(animal: Animal) -> None:
    print(animal.falar())


fazer_barulho(Cachorro())
fazer_barulho(Gato())
fazer_barulho(Cavalo())