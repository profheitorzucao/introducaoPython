from typing import Callable

minha_funcao:Callable[[int, int], int] = lambda x,y: x+y
print(minha_funcao(2,3))

minha_classe = type("MinhaClasse", (object,), {"nome": "Heitor", "meumetodo": lambda self: print(f"Nome= {self.nome}")})()

minha_classe.meumetodo()
minha_classe.Nome = "teste"

