luku = int(input('Syötä kokonaisluku: '))

if luku == 1:
    print('1 ei ole alkuluku')

else:

    for i in range(2, luku):
        if luku % i == 0:
            print(f'{luku} ei ole alkuluku')
            break
    else:
        print(f'{luku} on alkuluku!')
