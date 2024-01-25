lista = []
while True:
    luvut = (input('Syötä lukuja: '))
    if luvut == ' ':
        break
    luvut = float(luvut)
    lista.append(luvut)
lista.sort(reverse=True)
print(lista)
