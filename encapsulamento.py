class Professor:
    _Nome = None
    __Salario = None

professor1 = Professor

professor1._Nome = "Heitor"
professor1.__Salario = 1000

print(professor1._Nome)
print(professor1.__Salario)