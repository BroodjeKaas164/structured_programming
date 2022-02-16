def seizoen(maandje):
    if (maandje < 1) or (maandje > 12):
        return 'Maandnummer is ongeldig'
    else:
        if 3 < maandje <= 5:
            return 'Lente'
        elif 6 < maandje <= 9:
            return 'Zomer'
        elif 10 < maandje <= 11:
            return 'Herfst'
        else:
            return 'Winter'


print('Deze maand hoort bij: >>> ', seizoen(int(input('Maandnummer: >>> '))))
