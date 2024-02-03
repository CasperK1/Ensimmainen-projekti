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


def etaisyys(icao_1, icao_2):
    from geopy import distance
    yk, kursori = yhteys()

    kentta_1_kysely = (f"SELECT airport.latitude_deg, airport.longitude_deg "
                       f"FROM airport "
                       f"WHERE airport.ident = '{icao_1}'")
    kursori.execute(kentta_1_kysely)
    etaisyys_1 = kursori.fetchall()
    # Tarkastaa löytyykö etaisyys_1 tietokannasta
    if not etaisyys_1:
        print(f"Kenttää 1. {icao_1} ei löytynyt.")
        return


    kentta_2_kysely = (f"SELECT airport.latitude_deg, airport.longitude_deg "
                       f"FROM airport "
                       f"WHERE airport.ident = '{icao_2}'")
    kursori.execute(kentta_2_kysely)
    etaisyys_2 = kursori.fetchall()
    #Tarkastaa löytyykö etaisyys_2 tietokannasta
    if not etaisyys_2:
        print(f"Kenttää 2. {icao_2} ei löytynyt.")
        return

    print(f'Kentän {icao_1} ja {icao_2} välinen etäisyys: {distance.distance(etaisyys_1, etaisyys_2).km:.2f} km')


icao1 = input('Syötä 1. kentän ICAO-koodi: ')
icao_2 = input('Syötä 2. kentän ICAO-koodi: ')
etaisyys(icao1.upper(), icao_2.upper())
