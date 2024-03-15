import random


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

    def kulje(self):
        self.matka += self.hetkellinen_nopeus


def autojen_luonti():
    for x in range(1, 11):
        kisaajat.append(Auto(f'ABC-{x}', random.randint(100, 200)))
    return kisaajat


kisaajat = []
autojen_luonti()

while True:
    for auto in kisaajat:
        kiihdytys = random.randint(-10, 15)
        auto.nopeus(kiihdytys)
        auto.kulje() # 1 'tunti'

        if auto.matka >= 13626:  # Kilometriä
            break
    else:
        continue
    break



print(f'\n🥇Voittaja🥇: {auto.reknro} Huippunopeus: {auto.huippunopeus} km/h Matka: {max(auto.matka for auto in kisaajat)} km!\n')
print(f'╔{'═'*50}╗')
print(f'║Kilpailija ║ Huippunopeus (km/h)║Ajettu matka (km)║')
for auto in kisaajat:
        print(f'║{auto.reknro:^11}║{auto.huippunopeus:^20}║{auto.matka:^17}║')
print(f'╚{'═'*50}╝')
