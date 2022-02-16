#!/usr/bin/env python
# -*- coding: utf-8 -*-

# GitHub aanmaken en voeg DavidIsaacspaternostro@hu.nl toe in Mastermind

"""
Oriëntatie op AI

Bonusvraag: vier kwadraten

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht: werk onderstaande functies uit.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van pytest, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""


def vier_kwadraten(kwadraatsom):
    """
    Geef een lijst met vier getallen, zodat de som van de kwadraten van die
    getallen gelijk is aan gegeven kwadraatsom (int).
    """
    factorlst = [factor for factor in range(1, int(kwadraatsom / 2)) if factor ** 2 <= kwadraatsom]

    log_file = 'y'
    starttijd = perf_counter()
    for getal1 in factorlst:
        kwadtal1 = getal1 ** 2
        for getal2 in factorlst:
            kwadtal2 = getal2 ** 2
            if kwadtal1 <= kwadraatsom and kwadtal2 + kwadtal1 <= kwadraatsom:
                for getal3 in factorlst:
                    kwadtal3 = getal3 ** 2
                    if kwadtal2 <= kwadraatsom and kwadtal3 + kwadtal2 + kwadtal1 <= kwadraatsom:
                        for getal4 in range(max(factorlst), 1, -1):
                            rest = kwadraatsom - kwadtal1 - kwadtal2 - kwadtal3 - (getal4 ** 2)
                            if rest % getal4 == 0 and rest == 0:
                                if log_file == 'y' and getal1 > 7:
                                    with open(__getalfile(), "a") as file:
                                        file.write(
                                            f"{kwadraatsom}, {getal1, getal2, getal3, getal4}, {(perf_counter() - starttijd) * 1000:.0f}ms\n")
                                        file.close()
                                print(
                                    f"Done! \x1b[31m({kwadraatsom})\x1b[32m = \x1b[31m{getal1, getal2, getal3, getal4}^2\x1b[32m (Serie: \x1b[31m{getal1}\x1b[32m |"
                                    f" Tijd: \x1b[31m{(perf_counter() - starttijd) * 1000:.0f}ms\x1b[32m)")
                                return [getal1, getal2, getal3, getal4]


def __getalfile():
    return 'lastige_getallen.txt'


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
from functools import reduce
import random
from time import perf_counter


def test_vier_kwadraten():
    # Simulated test cases
    for cnt in range(100):
        n = random.randrange(1, 10)

        for _ in range(4):
            n *= 10
            n += random.randrange(0, 10)

        lst = vier_kwadraten(n)
        assert len(lst) == 4, \
            f"Fout: vier_kwadraten() geeft geen lijst met 4 maar met {len(lst)} getallen, namelijk {lst}"
        assert n == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({n}) geeft {lst}, maar {lst[0]}² + {lst[1]}² + {lst[2]}² + {lst[3]}² != {n}"


def test_vier_kwadraten_tijd():
    # Test cases
    testcases = [36624, 73504, 54296, 40923, 33504, 42627, 70798, 90815, 55367, 52699]

    for case in testcases:
        print(case)
        lst = vier_kwadraten(case)
        assert len(lst) == 4, \
            f"Fout: vier_kwadraten() geeft geen lijst met 4 maar met {len(lst)} getallen, namelijk {lst}"
        assert case == reduce(lambda x, y: x + y, (map(lambda x: x ** 2, lst))), \
            f"Fout: vier_kwadraten({case}) geeft {lst}, maar {lst[0]}² + {lst[1]}² + {lst[2]}² + {lst[3]}² != {case}"


if __name__ == '__main__':
    try:
        print("\x1b[32m")
        start_time = perf_counter()
        test_vier_kwadraten()
        delta_time = perf_counter() - start_time
        print(f"\t\tTotale tijd: {delta_time:.3f}s\n")
        print("Je functie vier_kwadraten(getal) werkt goed!\n")

        print("\x1b[0mTiming van 10 getallen...")

        start_time = perf_counter()
        test_vier_kwadraten_tijd()
        delta_time = perf_counter() - start_time
        print(f"\t\tTotale tijd: {delta_time * 1000:.0f}ms")

    except AssertionError as ae:
        print(f"\x1b[31m{ae}")
