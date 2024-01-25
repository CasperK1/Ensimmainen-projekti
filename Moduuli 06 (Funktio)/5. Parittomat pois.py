def parittomat_pois(luvut):
    parittomat_pois = []
    for i in luvut:
        if i % 2 == 0:
            parittomat_pois.append(i)
    return parittomat_pois


luvut = [1, 2, 3, 4, 5]

uudet_luvut = parittomat_pois(luvut)
print(f'Lista ilman parittomia lukuja: {uudet_luvut}')
