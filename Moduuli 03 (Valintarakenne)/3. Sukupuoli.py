sukupuoli=(input('Syötä sukupuoli (M/N): '))
sukupuoli=sukupuoli.upper()
hg=int(input('Hemoglobiini: '))
if sukupuoli=='M':
    if hg >= 134 and hg<= 195:
        print('Hemoglobiini normaali')
    elif hg < 134:
        print('Hemoglobiini alhainen')
    else:
        print('Hemoglobiini korkea')

if sukupuoli=='N':
    if hg >= 117 and hg<= 175:

        print('Hemoglobiini normaali')
    elif hg < 117:
        print('Hemoglobiini alhainen')
    else:
        print('Hemoglobiini korkea')


