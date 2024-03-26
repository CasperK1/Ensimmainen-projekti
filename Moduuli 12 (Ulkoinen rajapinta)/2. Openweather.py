import requests

while True:
    api = 'API KEY HERE'
    xy = input('\nPaikkakunta: ')
    try:
        req = requests.get(f'https://api.openweathermap.org/data/2.5/'
                           f'weather?q={xy}&APPID={api}&units=metric').json()

        print(f'{req["name"]} Maassa: {req["sys"]["country"]}\n')
        v = int(input('1. Säätiedot:  2. Uusi haku: '))
        if v == 1:
            print(f'\nSää {req["name"]}:')
            print(f'{req["main"]["temp"]} C°, {req["weather"][0]["main"]}')
            break

    except requests.exceptions.ConnectionError:
        print('Ei yhteyttä')
        break

    except Exception as e:
        print(f'Unexpected error occurred: {e}')
        if 'cod' in req and req['cod'] == '404':
            print('Paikkaa ei löytynyt\n')
        else:
            break