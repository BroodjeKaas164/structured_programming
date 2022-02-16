# Schrijf (en test) de functie kwadraten_som() die 1 parameter heeft: grondgetallen. Dit is een list is met integers.
# De return-waarde van de functie is de som van de kwadraten van alle positieve getallen in de lijst! Een lijst van [
# 4, 3, -5 ] heeft als return-waarde dus 25 (namelijk 16 + 9, want -5 is geen positief getal).
import random


def kwadraten_som(grondgetallen):
    som = 0
    for nummer in grondgetallen:
        if nummer >= 0:
            print("Positief: >>> " + str(nummer))
            som = som + nummer**2
    if som == 0:
        som = "Geen Positief aanwezig"
    print()
    return som


floating = [random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10), random.randint(-10, 10)]
print("Gegenereerd " + str(floating))
print()
print("Kwadraat van Positief: " + str(kwadraten_som(floating)))
