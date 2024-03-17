class Julkaisu:
    def __init__(self, nimi):
        self.nimi = nimi

    def tulosta_tiedot(self):
        print(f'{self.nimi}', end=' ')


class Lehti(Julkaisu):
    def __init__(self, nimi, toimittaja):
        super().__init__(nimi)
        self.toimittaja = toimittaja

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'(päätaomittaja {self.toimittaja})')


class Kirja(Julkaisu):
    def __init__(self, nimi, kirjailija, sivumaara):
        super().__init__(nimi)
        self.kirjailija = kirjailija
        self.sivumaara = sivumaara

    def tulosta_tiedot(self):
        super().tulosta_tiedot()
        print(f'(kirjailija {self.kirjailija}, {self.sivumaara} sivua)')


l = Lehti('Aku Ankka', 'Aki Hyyppä')
k = Kirja('Hytti n:o 6', 'Rosa Liksom', 200)
l.tulosta_tiedot()
k.tulosta_tiedot()
