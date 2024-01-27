def vuodenaika():
    vuodenaika = ('talvi', 'kevät', 'kesä', 'syksy')
    kuukausi = int(input('Anna kuukausi (1-12): '))
    if kuukausi == 12 or kuukausi == 1 or kuukausi == 2:
        print('Vuodenaika on', vuodenaika[0])
    elif kuukausi in range(3, 6):
        print('Vuodenaika on', vuodenaika[1])
    elif kuukausi in range(6, 9):
        print('Vuodenaika on', vuodenaika[2])
    elif kuukausi in range(9, 12):
        print('Vuodenaika on', vuodenaika[3])
    else:
        print('Virheellinen syöte!')

vuodenaika()