class Auto:
    def __init__(self, reknro, huippunopeus, hetkellinen_nopeus=0, matka=0):
        self.reknro = reknro
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.matka = matka

    def nopeus(self, kiihdytä):
        self.hetkellinen_nopeus += kiihdytä
        if self.hetkellinen_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus

        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0


auto_1 = Auto('ABC-123', 142)
print(f'Auton rekisterinumero: {auto_1.reknro}')
print(f'Huippunopeus: {auto_1.huippunopeus} km/h')
print(f'Auton nopeus: {auto_1.hetkellinen_nopeus} km/h')
print(f'Kuljettu matka: {auto_1.matka} km\n')

print('Kiihdytys...')
auto_1.nopeus(30)
auto_1.nopeus(70)
auto_1.nopeus(50)
print(f'Auton nopeus {auto_1.hetkellinen_nopeus} km/h\n')
auto_1.nopeus(-200)
print(f'Hätäjarrutus! Auton nopeus {auto_1.hetkellinen_nopeus} km/h')
