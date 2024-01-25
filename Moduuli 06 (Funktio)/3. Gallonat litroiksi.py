def gallonat(määrä):
    muunnos = määrä * 3.785
    if määrä == 1:
        print(f'{määrä} nestegallona on {muunnos} litraa')
    else:
        print(f'{määrä} nestegallonaa on {muunnos:.2f} litraa')


määrä = int(input('Syötä gallonat: '))

gallonat(määrä)
