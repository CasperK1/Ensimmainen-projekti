import random


def noppa():
    tulos = random.randint(1, 6)
    if tulos == 6:
        print(f'Tulos: {tulos}!!')
        return tulos
    else:
        print(f'Tulos: {tulos}')
        return tulos


while True:
    tulos = noppa()
    if tulos == 6:
        break
