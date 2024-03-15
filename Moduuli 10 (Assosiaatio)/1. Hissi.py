class Hissi:
    def __init__(self, alin_kerros, ylin_kerros):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.sijainti = alin_kerros

    def siirry_kerrokseen(self, siirry):
        if siirry > self.ylin or siirry < self.alin:
            print('Virheellinen kerros')
        else:
            while self.sijainti < siirry:
                self.kerros_ylos()
                print(self.sijainti)
            while self.sijainti > siirry:
                self.kerros_alas()
                print(self.sijainti)

    def kerros_ylos(self):
        self.sijainti += 1

    def kerros_alas(self):
        self.sijainti -= 1


h= Hissi(1,10)
h.siirry_kerrokseen(6)
h.siirry_kerrokseen(1)



