def analyzer(getallen):
    lijstje = getallen.split('-')
    lijstje.sort()

    nieuwLijst = []
    for nummer in range(1, len(lijstje)-1):
        nieuwLijst.append(int(lijstje[nummer]))

    maxim = max(nieuwLijst)
    minim = min(nieuwLijst)
    length = len(nieuwLijst)
    som = sum(nieuwLijst)
    gem = som / length

    """
    Gesorteerde list van ints: [1, 2, 3, 4, 5, 7, 7, 7, 8, 8, 9, 9] 
    Grootste getal: 9 en Kleinste getal: 1 
    Aantal getallen: 12 en Som van de getallen: 70 
    Gemiddelde: 5.833333333333333
    """

    return lijstje, maxim, minim, length, som, gem


print(analyzer("5-9-7-1-7-8-3-2-4-8-7-9"))
