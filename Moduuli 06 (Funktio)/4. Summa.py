def listan_summa(luvut):
    summa = 0
    for i in luvut:
        summa += i
    return summa


luvut = [1, 2, 3, 4, 5]

summa = listan_summa(luvut)
print(f'Listan summa: {summa}')
