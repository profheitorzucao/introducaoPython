import array

notas = array.array('f', [10, 9.5, 8, 10, 9.7])

media = 0.0

for nota in notas:
    media += nota

media = media/notas.__len__()

print(f"A sua média é: {media}")