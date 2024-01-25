import random

kuutioiden_summa=0
kuutiot = int(input('Arpakuutioiden määrä: '))
y=0
for _ in range(kuutiot):
    x= random.randint(1, 6)
    kuutioiden_summa += x

print(f'Kuutioiden silmälukujen summa {kuutioiden_summa}')