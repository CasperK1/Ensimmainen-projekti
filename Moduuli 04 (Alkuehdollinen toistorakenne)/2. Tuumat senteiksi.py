while True:
    x = float(input('Anna tuumat, negatiivinen luku lopettaa: '))
    if x < 0:
        break
    print(f'{x * 2.54:.2f} cm')
