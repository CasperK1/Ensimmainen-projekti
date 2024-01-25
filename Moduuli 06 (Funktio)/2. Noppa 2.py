import random


def noppa(silmät):
    tulos = random.randint(1, silmät)
    print(f'Tulos on {tulos}')
    return tulos


silmät = int(input('Anna silmäluku: '))
while noppa(silmät) != silmät:
    continue
