x = []
while True:
    luku = input('Anna luku, tyhjä syöte lopettaa: ')
    if luku == ' ' or luku == '':
        break
    x.append(int(luku))
if x:
    print(f'Pienin {min(x)} ja suurin {max(x)}')
else:
    print('Yhtään lukua ei syötetty')
