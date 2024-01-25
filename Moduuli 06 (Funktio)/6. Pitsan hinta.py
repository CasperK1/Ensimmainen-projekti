import math


def pitsan_arvo(d, v):
    d = float(d)
    v = float(v)
    d_2 = ((d / 2) * 2 * math.pi) / 10000
    d_2 = v / d_2
    return d_2


pitsa_1 = input('Syötä 1. pitsan halkaisija (cm): ')
hinta_1 = input('Syötä 1. pitsan hinta euroina: ')

pitsa_2 = input('Syötä 2. pitsan halkaisija (cm): ')
hinta_2 = input('Syötä 2. pitsan hinta euroina: ')

pitsa_1 = pitsan_arvo(pitsa_1, hinta_1)
pitsa_2 = pitsan_arvo(pitsa_2, hinta_2)

if pitsa_1 < pitsa_2:
    print('1. pitsa on parempaa vastinetta rahalle')
if pitsa_1 > pitsa_2:
    print('2. pitsa on parempaa vastinetta rahalle')
else:
    print('Molemmat ovat yhtä hyvää vastinetta rahalle!')