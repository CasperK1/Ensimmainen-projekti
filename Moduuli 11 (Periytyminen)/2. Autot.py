class Auto:
    def __init__(self, reknro, huippunopeus):
        self.reknro = reknro
        self.huippunopeus = huippunopeus
        self.matka = 0

    def kulje(self, tunnit, nopeus):
        self.matka += tunnit * nopeus
        print(f'{self.reknro} kuljettu matka: {self.matka} km. Matka-aika: {tunnit}h')


class Sahkoauto(Auto):
    def __init__(self, reknro, huippunopeus, akkukapasiteetti):
        super().__init__(reknro, huippunopeus)
        self.akkukapasiteetti = akkukapasiteetti


class Polttomoottori(Auto):
    def __init__(self, reknro, huippunopeus, bensatankki):
        super().__init__(reknro, huippunopeus)
        self.bensatankki = bensatankki


s = Sahkoauto('ABC-15', 180, 52.5)
b = Polttomoottori('ACD-123', 165, 32.3)

s.kulje(3, 120)
b.kulje(3, 100)
