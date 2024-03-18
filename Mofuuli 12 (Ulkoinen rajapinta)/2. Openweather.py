import requests

while True:
    xy = input('\nPaikkakunta: ')
    req = requests.get(f'https://api.openweathermap.org/data/2.5/'
                       f'weather?q={xy}&units=metric&APPID=2e58478f3f001fa2acb8c4c12460c90d').json()
    try:
        print(f'{req['name']} Maassa: {req['sys']['country']}\n')
        v = int(input('1. Säätiedot:  2. Uusi haku: '))
        if v == 1:
            print(f'\nSää {req['name']}:')
            print(f'{req['main']['temp']} C°, {req['weather'][0]['main']}')
            break

    except (KeyError, requests.exceptions.RequestException) as e:
        if req['cod'] == '404':
            print(f'Hakua ei löytynyt\n')
        else:
            print('Error')
