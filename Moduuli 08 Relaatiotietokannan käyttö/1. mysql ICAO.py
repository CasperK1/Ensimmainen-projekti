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
        print(f'Yhdistetty tietokantaan: {yk.database}')
        kursori = yk.cursor()
        return yk, kursori


def icao():
    yk, kursori = yhteys()
    sql = 'select airport.ident FROM airport'
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print(tulos)


icao()
