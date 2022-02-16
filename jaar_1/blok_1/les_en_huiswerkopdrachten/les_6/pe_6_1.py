def convert(celsius):
    fahrenheit = (celsius * 1.8) + 32
    return fahrenheit


def table():
    tabelletje = []
    for n in range(-30, 41, 10):
        x = convert(n)
        tabelletje.append(str(x))
        tabelletje.append(str(n))
        print('{:10} {:10}'.format(x, n))
    return tabelletje


print('{0:5}\t\t{1:5}'.format('     F', '     C'))
table()
