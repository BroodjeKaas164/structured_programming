woordenlijst = []
while True:
    try:
        woord = input("Geef een string van vier letters: >>> ")
        if len(woord) == 4:
            break
        else:
            print('{} heeft {} letters'.format(woord, len(woord)))
    except:
        print("\tDit is geen geldige invoer.")

print('Inlezen van correcte string: {} is geslaagd!'.format(woord))
