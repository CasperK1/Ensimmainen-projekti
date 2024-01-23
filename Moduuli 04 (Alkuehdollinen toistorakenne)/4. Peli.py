import random

x = random.randint(1, 10)
while True:
    s = int(input('Arvaa numero: '))
    if s == x:
        print('Oikein')
        break
    elif s < x:
        print('Liian pieni arvaus')
    else:
        print('Liian suuri arvaus')
