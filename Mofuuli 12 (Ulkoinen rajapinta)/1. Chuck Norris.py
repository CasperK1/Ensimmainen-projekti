import requests

req = requests.get('https://api.chucknorris.io/jokes/random').json()

print(req['value'])
