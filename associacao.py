class Endereco:
    def __init__(self, rua, cidade):
        self.Rua = rua
        self.Cidade = cidade
    def MostrarEndereco(self):
        print(f"Rua: {self.Rua}, cidade: {self.Cidade}")

class Pessoa():
    def __init__(self, nome, endereco):
        self.Nome = nome
        self.Endereco = endereco
    def apresentar(self):
        print(f"Ola meu nome é {self.Nome}")
        self.Endereco.MostrarEndereco()

endereco = Endereco("teste", "Araçatuba")
pessoa = Pessoa("Heitor", endereco)

pessoa.apresentar()

      