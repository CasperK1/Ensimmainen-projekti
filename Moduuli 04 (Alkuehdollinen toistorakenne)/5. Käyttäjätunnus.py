id = 'python'
passw = 'rules'

kokeilu = 0

while True:
    id2 = input('Syötä tunnus: ')
    passw2 = input('Syötä salasana: ')
    if id2 == id and passw == passw2:
        print('Tervetuloa')
        break
    else:
        kokeilu += 1
        if kokeilu == 5:
            print('Pääsy evätty')
            break
