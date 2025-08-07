nome = None

print("Hello world!")

nome = input("Digite seu nome: ")

print("Seu nome é: "+nome+". Parabens")
print(f"Seu nome é: {nome}. Parabens")

sexo = input("Digite seu sexo biologico F - Feminino M - Masculino")

if sexo == "M":
    aposenta = 65
elif sexo == "F":
    aposenta = 60
else:
    print("Sexo invalido considere informar F ou M")
    exit()

idade = int(input("Digite sua idade:" ))

tempoaposenta = aposenta - idade

print(f"Falta {tempoaposenta} anos para você se aposentar")

