from flask import Flask

app = Flask(__name__)


@app.route('/<arvo>')
def alkuluku(arvo):
    arvo = int(arvo)
    if arvo == 1:
        vastaus = {'Number': arvo, 'isPrime': False}
        return vastaus

    else:
        for i in range(2, arvo):
            if arvo % i == 0:
                vastaus = {'Number': arvo, 'isPrime': False}
                return vastaus
        else:
            vastaus = {'Number': arvo, 'isPrime': True}
            return vastaus


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
