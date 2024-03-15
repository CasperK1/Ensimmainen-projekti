class Talo:
    def __init__(self, alin_kerros, ylin_kerros, hissien_lkm):
        self.alin = alin_kerros
        self.ylin = ylin_kerros
        self.hissien_lkm = hissien_lkm
        self.hissien_lista = [Hissi(self.alin, self. ylin) for _ in range(self.hissien_lkm)]

    def aja_hissia(self, hissin_nro, kerros):
        self.hissien_lista[hissin_nro].siirry_kerrokseen(kerros)
        print(f'Hissi nro. {hissin_nro} saapui kerrokseen: {self.hissien_lista[hissin_nro].sijainti}')

    def palohalytys(self):
        print(f'\nPalohälytys!')
        for _ in range(len(self.hissien_lista)):
            self.aja_hissia(_, self.alin)
        print(f'\nKaikki rakennuksen hissit alimmassa kerroksessa')




class Hissi:
    def __init__(self, talon_alin_kerros, talon_ylin_kerros):
        self.alin = talon_alin_kerros
        self.ylin = talon_ylin_kerros
        self.sijainti = talon_alin_kerros

    def siirry_kerrokseen(self, siirry):
        if siirry > self.ylin or siirry < self.alin:
            print('Virheellinen kerros')
        else:
            while self.sijainti < siirry:
                self.kerros_ylos()
            while self.sijainti > siirry:
                self.kerros_alas()

    def kerros_ylos(self):
        self.sijainti += 1

    def kerros_alas(self):
        self.sijainti -= 1

t = Talo(1,5,3)

t.aja_hissia(0,4)
print(t.hissien_lista[0].sijainti)

t.palohalytys()