from flask import Flask


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


app = Flask(__name__)


@app.route('/<icao>')
def icao(icao):
    yk, kursori = yhteys()
    sql = (f"SELECT airport.name, airport.municipality FROM airport "
           f"WHERE airport.ident = '{icao}'")
    kursori.execute(sql)
    query = kursori.fetchall()
    if not query:
        tulos = {'icao': icao, 'message': 'not found'}
        return tulos
    else:
        tulos = {'ICAO': icao, 'Name': query[0][0], 'Municipality': query[0][1]}
        return tulos


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
