leiviskat=float(input('Anna leiviskät: '))
naulat=float(input('Anna naulat: '))
luodit=float(input('Anna luodit: '))

naulat_si= naulat * 425.6
luodit_si= luodit * 13.3
leiviskat_si= leiviskat * 8512

grammat=naulat_si+luodit_si+leiviskat_si
print('Massa nykymittojen mukaan:')
print((int(grammat//1000)),'kilogrammaa ja', round(grammat%1000, 2),'grammaa.')
