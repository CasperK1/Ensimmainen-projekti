import random


class Kilpailu:
    def __init__(self, nimi, matka, kilpailijat_lista):
        self.kilpailun_nimi = nimi
        self.matka = matka
        self.kilpailijat = kilpailijat_lista

    def tunti_kuluu(self):

        for auto in self.kilpailijat:
            auto.nopeus(random.randint(-10, 15))
            auto.kulje()  # 1 'tunti'

            if auto.matka >= 8000:
                print(f'\nKisa ohi')
                print(f'🥇Voittaja🥇: {auto.reknro} Huippunopeus: {auto.huippunopeus} km/h '
                      f'Matka: {auto.matka} km!\n')

                self.tulosta_tilanne()

    def tulosta_tilanne(self):

        print(f'╔{'═' * 50}╗')
        print(f'║Kilpailija ║ Huippunopeus (km/h)║Ajettu matka (km)║')
        for auto in self.kilpailijat:
            print(f'║{auto.reknro:^11}║{auto.huippunopeus:^20}║{auto.matka:^17}║')
        print(f'╚{'═' * 50}╝')

    def kilpailu_ohi(self):
        return any(auto.matka >= self.matka for auto in self.kilpailijat)


class Auto:
    def __init__(self, reknro, huippunopeus, hetkellinen_nopeus=0, matka=0):
        self.reknro = reknro
        self.huippunopeus = huippunopeus
        self.hetkellinen_nopeus = hetkellinen_nopeus
        self.matka = matka

    def nopeus(self, kiihdyta):
        self.hetkellinen_nopeus += kiihdyta
        if self.hetkellinen_nopeus > self.huippunopeus:
            self.hetkellinen_nopeus = self.huippunopeus

        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0

    def kulje(self):
        self.matka += self.hetkellinen_nopeus


def kilpailun_luonti():
    kisaajat = [Auto(f'ABC-{x}', random.randint(100, 200)) for x in range(10)]
    kilpailu = Kilpailu('Suuri Romuralli', 8000, kisaajat)
    return kilpailu


def main():
    kisa = kilpailun_luonti()
    tunnit = 0
    while not kisa.kilpailu_ohi():
        kisa.tunti_kuluu()
        tunnit += 1
        if tunnit % 10 == 0:
            print(f'\nTilanne {tunnit}h kohdalla: ')
            kisa.tulosta_tilanne()


main()
