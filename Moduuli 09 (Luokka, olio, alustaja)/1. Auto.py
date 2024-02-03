class Auto:
    def __init__(self, reknro, huippunopeus):
        self.reknro = reknro
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = 0
        self.matka = 0


auto_1 = Auto('ABC-123', 142)
print(f'Auton rekisterinumero: {auto_1.reknro}')
print(f'Huippunopeus: {auto_1.huippunopeus} km/h')
print(f'Auton nopeus: {auto_1.hetkellinen_nopeus} km/h')
print(f'Kuljettu matka: {auto_1.matka} km')