class Auto:
    def __init__(self, reknro, hnopeus=0, matka=0):
        self.reknro = reknro
        self.hnopeus = hnopeus
        self.matka = matka


auto_1 = Auto('ABC-123', 142)
print(f'Auton rekisterinumero: {auto_1.reknro}')
print(f'Huippunopeus {auto_1.hnopeus} km/h')
