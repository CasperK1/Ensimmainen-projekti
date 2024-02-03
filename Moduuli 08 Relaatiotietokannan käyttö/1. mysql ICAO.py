def yhteys():
    import mysql.connector
    yk = mysql.connector.connect(
        host='127.0.0.1',
        port=3306,
        database='flight_game',
        user='root',
        password='root',
        autocommit=True)
    # Yhteystesti, yhdistetyn tietokannan nimi, kursorin ja tietokannan palautus pääohjelmaan
    if yk.is_connected():
        print(f'Yhdistetty tietokantaan: {yk.database}\n')
        kursori = yk.cursor()
        return yk, kursori


def icao(icao_syote):
    yk, kursori = yhteys()
    sql = (f"SELECT airport.name, airport.municipality FROM airport "
           f"WHERE airport.ident = '{icao_syote}'")
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if not tulos:
        print(f"Kenttää {icao_syote} ei löytynyt.")
        return
    print(f'Kenttä {icao_syote} on nimeltään {tulos[0][0]}, joka sijaitsee kunnassa {tulos[0][-1]}.')


icao_syote = input('Syötä ICAO: ')

icao(icao_syote.upper())
