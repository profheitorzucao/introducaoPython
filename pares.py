import array

numeros = array.array('i', [])

for v in range(10):
    numeros.append(int(input(f"Digite um numero inteiro: ")))

for numero in numeros:
    if numero%2 == 0:
        print(numero)