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


def etaisyys(icao1, icao2):
    from geopy import distance
    yk, kursori = yhteys()

    sql = (f"SELECT airport.latitude_deg, airport.longitude_deg "
           f"FROM airport "
           f"WHERE airport.ident = '{icao1}'")
    kursori.execute(sql)
    etaisyys1 = tuple(kursori.fetchall())

    sql = (f"SELECT airport.latitude_deg, airport.longitude_deg "
           f"FROM airport "
           f"WHERE airport.ident = '{icao2}'")
    kursori.execute(sql)
    etaisyys2 = tuple(kursori.fetchall())

    print(f'Kentän {icao1} ja {icao2} välinen etäisyys: {distance.distance(etaisyys2, etaisyys1)}')


icao1 = input('Syötä 1. kentän ICAO-koodi: ')
icao2 = input('Syötä 2. kentän ICAO-koodi: ')
etaisyys(icao1, icao2)
