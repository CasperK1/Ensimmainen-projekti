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
            return
        if self.hetkellinen_nopeus < 0:
            self.hetkellinen_nopeus = 0
            return

    def kulje(self, tunnit):
        self.matka += tunnit * self.hetkellinen_nopeus

# Auton parametri 'matka' arvo on kilometreissä
auto_1 = Auto('ABC-123', 142, 50, 0)

auto_1.kulje(1)
print(auto_1.matka)
