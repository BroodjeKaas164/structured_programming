import random

"""
Hieronder staan de functies die worden gebruikt om de prijs te berekenen van de treinrit,
rekening houdende met de voorgeschreven voorwaarden.
"""


def standaardprijs(afstandKM):
    if afstandKM >= 0:
        if afstandKM <= 50:
            prijs = afstandKM * 0.80
        else:
            prijs = (afstandKM * 0.60) + 15
    else:
        prijs = 0
    return prijs


def ritprijs(leeftijd, weekendrit, afstandKM):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijsMK = standaardprijs(afstandKM) * 0.65
        else:
            prijsMK = standaardprijs(afstandKM) * 0.6
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijsMK = standaardprijs(afstandKM) * 0.7
        else:
            prijsMK = standaardprijs(afstandKM)
    return prijsMK


"""
Hieronder staan de willekeurig gegenereerde: 
- leeftijd 
- true-false statement
- en de afstand van de rit in kilometers 
gedeclareerd.
"""

leeftijdje = random.randint(9, 68)
weekndbool = random.uniform(0, 1) < 0.5
afstandje = random.randint(-40, 120)

print("Leeftijd: >>>", str(leeftijdje))
print("Weekendrit: >>>", str(weekndbool))
print("Afstand in kilometers: >>>", str(afstandje))

print()
print("Prijs van treinrit: >>> €", round(ritprijs(leeftijdje, weekndbool, afstandje), 2))

"""
Hieronder word aangegeven welke formule is gebruikt om bij het antwoord te komen
"""


def standaardprijsformule(afstandKM):
    if afstandKM >= 0:
        if afstandKM <= 50:
            prijs = str(afstandKM) + " * 0.80"
        else:
            prijs = "(" + str(afstandKM) + " * 0.60) + 15"
    else:
        prijs = 0
    return prijs


def ritprijsformule(leeftijd, weekendrit, afstandKM):
    if weekendrit:
        if leeftijd < 12 or leeftijd >= 65:
            prijsMK = (str(round(standaardprijs(afstandKM), 2)) + " * 0.65")
        else:
            prijsMK = (str(round(standaardprijs(afstandKM), 2)) + " * 0.6")
    else:
        if leeftijd < 12 or leeftijd >= 65:
            prijsMK = (str(round(standaardprijs(afstandKM), 2)) + " * 0.7")
        else:
            prijsMK = (str(round(standaardprijs(afstandKM), 2)))
    return prijsMK


print()
print("Gebruikte formule: >>> Afstand van de rit =", afstandje, "dus:", standaardprijsformule(afstandje), "= €", round(standaardprijs(afstandje), 2),
      ", en weekendrit =", weekndbool, ", en leeftijd is", leeftijdje, ", dus:", str(ritprijsformule(leeftijdje, weekndbool, afstandje)), "= €", str(round(ritprijs(leeftijdje, weekndbool, afstandje), 2)))
