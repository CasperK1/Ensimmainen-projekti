def nimet():
    nimet = set()
    while True:
        nimi = input("Nimi, enter lopettaa: ")
        if nimi == "" or nimi == " ":
            break
        elif nimi in nimet:
            print('Aiemmin syötetty nimi.')
        else:
            nimet.add(nimi)
            print('Uusi nimi')
    for i in nimet:
        print(i)
nimet()