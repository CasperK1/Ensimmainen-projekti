v=int(input("Syötä vuosi: "))

if v<100:
    if v%4==0:
        print(v,'on karkausvuosi')
    else:
        print(v,'ei ole karkausvuosi')
else:
    if v%100==0 and v%400==0:
        print(v,'on karkausvuosi')
    else:
        print(v,'ei ole karkausvuosi')