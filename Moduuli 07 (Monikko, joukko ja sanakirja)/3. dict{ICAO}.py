lentokentät = {
    "EFHK": "Helsinki-Vantaan lentoasema",
    "EFTU": "Turun lentoasema",
    "EFTP": "Tampere-Pirkkalan lentoasema",
    "EFOU": "Oulun lentoasema",
    "EFJY": "Jyväskylän lentoasema",
    "EFRO": "Rovaniemen lentoasema",
    "EFKU": "Kuopion lentoasema",
    "EFVA": "Vaasan lentoasema",
    "EFLP": "Lappeenrannan lentoasema",
    "EFJO": "Joensuun lentoasema",
    "EFKT": "Kittilän lentoasema",
    "EFIV": "Ivalon lentoasema",
    "EFMA": "Maarianhaminan lentoasema",
}


def lentoasema_kysely():
    while True:
        x = input('Hae kenttän nimeä ICAO-koodilla (H), lisää kenttä (L), lopeta (Q): ')

        if x.upper() == 'H':
            haku = input('Syötä ICAO: ')
            if lentokentät.get(haku.upper()) is None:
                print('Kenttää ei löytynyt, tarkasta ICAO ja tarvittaessa lisää uusi kenttä')
            else:
                print(f'Kentän nimi: {lentokentät.get(haku.upper())}')

        elif x.upper() == 'L':
            icao = input('Syötä ICAO: ')
            kenttä = input('Syötä kenttä: ')
            lentokentät[icao] = kenttä.capitalize()
            print(f'Uusi kenttä lisätty {icao}: {kenttä}')

        elif x.upper() == 'Q':
            break
        else:
            print('Virheellinen syöte!')


lentoasema_kysely()
