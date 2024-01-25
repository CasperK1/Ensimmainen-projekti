import random

pisteet = int(input('Arvottavien pisteiden määrä: '))

pisteet_sisällä = 0

for i in range(pisteet):
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)

    if x ** 2 + y ** 2 < 1:
        pisteet_sisällä += 1

pi = 4 * pisteet_sisällä / pisteet
print(f'Piin likiarvo {pisteet} pisteellä on: {pi}')
