class Departamento:
    def __init__(self, nome):
        self.Nome = nome
        self.Professores = []
    def AdicionarProfessor(self, professor):
        self.Professores.append(professor)
    def Imprimir(self):
        print(f"Departamento: {self.Nome} tem o seguintes professores:")
        for p in self.Professores:
            print(f"Professor: {p.Nome}")

class Professor:
    def __init__(self, nome):
        self.Nome = nome
        
professor = Professor('Heitor')
professor1 = Professor("Fabiano")
departamento = Departamento("Tecnologia da Informação")
departamento.AdicionarProfessor(professor)
departamento.AdicionarProfessor(professor1)
departamento.Imprimir()