#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 2: algoritmiek

(c) 2019 Hogeschool Utrecht,
Tijmen Muller (tijmen.muller@hu.nl)

Opdracht:
Beantwoord onderstaande vragen en werk onderstaande functies uit.
Voeg commentaar toe om je code toe te lichten.

Je kunt je functies testen met het gegeven raamwerk door het bestand
uit te voeren (of met behulp van `pytest`, als je weet hoe dat werkt).
Lever je werk in op Canvas als alle tests slagen.

Let op! Het is niet toegestaan om bestaande modules te importeren en te
        gebruiken, zoals `math` en `statistics`.
"""

naam = "Delano Tjon-A-Njoek"
klas = "TICT-V1D-Team4"
studentnummer = 1814947

"""
1.  Sorteeralgoritme

    Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    1a. Handmatig toepassen
        Gegeven is de lijst l = [ 4, 3, 1, 2 ]. Geef de waardes die deze
        lijst aanneemt bij álle tussenstappen bij toepassing van
        bovenstaand sorteeralgoritme.
"""
# TODO: 1a
# [4, 3, 1 ,2] Begintoestand
# [3, 4, 1 ,2]
# [3, 1, 4 ,2]
# [1, 3, 4, 2]
# [1, 3, 2, 4]
# [1, 2, 3 ,4] Beoogde Doel
"""
    1b. Implementatie
        Implementeer het sorteeralgoritme in Python in een functie
        hieronder genaamd my_sort(lst).

    1c. Best en worst case
        -   Stel je hebt een lijst met de waarden 1, 2 en 3. Bij welke
            volgorde van de waarden in de lijst is het sorteeralgoritme
            het snelste klaar (best-case scenario)?
            Hoeveel vergelijkingen (zoals beschreven in stap 1. van de
            pseudocode) zijn nodig geweest?
"""
# TODO: 1c
# Het programma is best-case scenario klaar in 2 vergelijking(en).
# toelichting:
#       [(1, 2), 3]
#       [1, (2, 3)]
"""
        -   Bij welke volgorde van de waarden in de lijst is het
            sorteeralgoritme het minst snel klaar (worst-case scenario)?
            Hoeveel vergelijkingen zijn nodig geweest?
"""
# TODO: 1c / vervolg 1
# Er is sprake van en worst-case-scenario, als de lijst getallen van groot naar klein geordend is.
# Er zijn 6 vergelijkingen nodig [3, 2, 1]
# Toelichting:
#       [(3, 2), 1]
#       [2, (3, 1)]
#       [(2, 1), 3]
#       [1, (2, 3)]
#       [(1, 2), 3]
#       [1, (2, 3)]
"""
        -   Stel je hebt een lijst met de waarden 1 tot en met 4.
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
# TODO: 1c / vervolg 2
# De best-case scenario zal alleen plaatsvinden als de lijst al gesorteerd is.
# Er zijn 3 vergelijkingen nodig [1, 2, 3, 4]
# Toelichting:
#       [(1, 2), 3, 4]
#       [1, (2, 3), 4]
#       [1, 2, (3, 4)]

# De worst-case scenario zal alleen plaatsvinden als de lijst getallen van groot naar klein geordend is.
# Er zijn 12 vergelijkingen nodig [4, 3, 2, 1]
# Toelichting:
#       [(4, 3), 2, 1]
#       [3, (4, 2), 1]
#       [3, 2, (4, 1)]
#       [(3, 2), 1, 4]
#       [2, (3, 1), 4]
#       [2, 1, (3, 4)]
#       [(2, 1), 3, 4]
#       [1, (2, 3), 4]
#       [1, 2, (3, 4)]
#       [(1, 2), 3, 4]
#       [1, (2, 3), 4]
#       [1, 2, (3, 4)]
"""
        -   Stel je hebt een lijst met de waarden 1 tot en met n
            (je weet nu dus niet precies hoeveel waarden er in de lijst
            zitten, het zijn er 'n').
            Wat is nu het best-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
            En wat is nu het worst-case scenario?
            Hoeveel vergelijkingen zijn er nodig?
"""
# TODO: 1c / vervolg 3
# De best-case scenario zal alleen plaatsvinden als de lijst al gesorteerd is.
# Er zijn n-1 vergelijkingen nodig

# De worst-case scenario zal alleen plaatsvinden als de lijst getallen van groot naar klein geordend is.
# Er zijn n(n-1) vergelijkingen nodig, met n = len(lst)
# Toelichting:
#       [3, 2, 1] | n = 3 daarmee 3(3-1) = 6 | Zie toelichting 1c / vervolg 1
#       [4, 3, 2, 1] | n = 4 daarmee 4(4-1) = 12 | Zie toelichting 1c / vervolg 2
#       [5, 4, 3, 2, 1] | n = 5 daarmee 5(5-1) = 20 | Bewezen via testraamwerk
#       [6, 5, 4, 3, 2, 1] | n = 6 daarmee 6(6-1) = 30 | Bewezen via testraamwerk


def my_sort(lst):
    """
    Sorteer gegeven lijst volgens het algoritme zoals beschreven in de pseudocode.

    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1.

    Zorg dat de gegeven lijst niet verandert, maar geef een nieuwe, gesorteerde variant van de lijst terug.

    Args:
        lst: (list): Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.

    Returns:
        list: Een nieuwe, gesorteerde variant van lijst `lst`.
    """
    """Hieronder staat de pseudocode van een sorteeralgoritme:
    1. Startend vanaf het begin van een lijst, vergelijk elk element met zijn volgende buur.
    2. Als het element groter is dan zijn volgende buur, verwissel ze van plaats.
    3. Doorloop zo de lijst tot het eind.
    4. Als er verwisselingen zijn geweest bij stap 2., ga naar stap 1."""

    lst_sorted = lst.copy()
    # steps = 0
    state = False
    while not state:
        state = True
        for x in range(len(lst_sorted) - 1):
            # steps += 1
            if lst_sorted[x + 1] < lst_sorted[x]:
                lst_sorted[x], lst_sorted[x + 1] = lst_sorted[x + 1], lst_sorted[x]
                state = False
    # print(steps)
    return lst_sorted


def linear_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief lineair zoeken.

    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    """
    Maak kopie van lijst
    als de lijst index 0 gelijk staat aan doelgetal
        Geef True terug
    als de lengte van de lijst 1 is EN lijst is niet doelgetal
        Geef False terug
    anders
        roep functie opnieuw aan met vernieuwde 0 index
    """

    lstcopy = lst.copy()
    if lstcopy[0] == target:
        return True
    if len(lstcopy) == 1 and lstcopy != target:
        return False
    else:
        lstcopy.remove(lstcopy[0])
        return linear_search_recursive(lstcopy, target)


def binary_search_recursive(lst, target):
    """
    Zoek een element in de gegeven lijst door middel van recursief binair zoeken.

    Je mag ervan uit gaan dat de gegeven lijst al gesorteerd is.
    Zorg dat de inhoud van de gegeven lijst niet verandert.

    Args:
        lst (list):     Een lijst met elementen van gelijk type, bijvoorbeeld gehele getallen.
        target (int):   Het gezochte element.

    Returns:
        bool: Of het element in de lijst voorkomt.
    """
    """
    bereken midden van lijst
    
    if index gemiddelde in lijst het doelgetal is:
        return True
    anders als de lengte van de lijst gelijk staat aan 1 EN is niet doelgetal:
        return False
        
    als index gemiddelde in lijst kleiner is dan doelgetal:
        roep functie opnieuw aan met nieuwe lijst
    als index gemiddelde in lijst grote is dan target:
        roep functie opnieuw aan met nieuwe lijst
    """

    guess = int(len(lst) // 2)

    if lst[guess] == target:
        return True
    elif len(lst) == 1 and lst[guess] != target:
        return False

    if lst[guess] < target:
        return binary_search_recursive(lst[guess:], target)
    elif lst[guess] > target:
        return binary_search_recursive(lst[:guess], target)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""
import random


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_my_sort():
    lst_test = random.choices(range(-99, 100), k=6)
    lst_test = [6, 5, 4, 3, 2, 1]
    lst_copy = lst_test.copy()
    lst_output = my_sort(lst_test)

    assert lst_copy == lst_test, "Fout: my_sort(lst) verandert de inhoud van lijst lst"
    assert lst_output == sorted(lst_test), \
        f"Fout: my_sort({lst_test}) geeft {lst_output} in plaats van {sorted(lst_test)}"


def test_linear_search_recursive():
    for _ in range(10):
        lst_test = random.sample(range(20), 6)
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = linear_search_recursive(lst_test, target)
        assert lst_copy == lst_test, "Fout: linear_search_recursive(lst, target) verandert de inhoud van lijst lst"
        assert outcome == found, \
            f"Fout: linear_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"


def test_binary_search_recursive():
    for _ in range(10):
        lst_test = sorted(random.sample(range(20), 6))
        target = random.randrange(20)
        found = target in lst_test
        lst_copy = lst_test.copy()

        outcome = binary_search_recursive(lst_test, target)
        assert outcome == found, \
            f"Fout: binary_search_recursive({lst_test}, {target}) geeft {outcome} in plaats van {found}"
        assert lst_copy == lst_test, "Fout: binary_search_recursive(lst, target) verandert de inhoud van lijst lst"


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_my_sort()
        print("Je functie my_sort() werkt goed!")

        test_linear_search_recursive()
        print("Je functie linear_search_recursive() werkt goed!")

        test_binary_search_recursive()
        print("Je functie binary_search_recursive() werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")

    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()
