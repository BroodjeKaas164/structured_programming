#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Oriëntatie op AI

Final assignment 1: getallen

(c) 2019 Hogeschool Utrecht,
Bart van Eijkelenburg en
Tijmen Muller (tijmen.muller@hu.nl)


Opdracht:
Werk onderstaande functies uit.
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


def is_even(n):
    """
    Bepaal of een getal even is.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als even, False als oneven.
    """
    """
    als n deelbaar is door 2 met restwaarde 0, is het getal even (True). Anders oneven (False)
    """
    if n % 2 == 0:
        return True
    else:
        return False


def floor(real):
    """ Bepaal het grootste gehele getal (int), dat kleiner dan of gelijk is aan real (float). """
    """
    in een range van -10000, 10000 met i == range(-10000, 10000)
        als i kleiner is dan of gelijk is aan het getal (real)
            JA: i wordt met 1 verhoogd
        als getal (real) == 0
            JA: geef 0 terug
        anders verlagen we i met 1 en geven we int(i) terug
    """
    for i in range(-10000, 10000):
        if i <= real:
            i = i + 1
        elif real == 0:
            return 0
        else:
            i = i - 1
            return int(i)

    """
    return int(real // 1 + 1)

    # Vereenvoudiging met operator; hetzelfde resultaat gerealiseerd
    """


def ceil(real):
    """ Bepaal het kleinste gehele getal (int), groter dan of gelijk aan real (float). """
    """
    Exacte spiegeling van f(floor):
    
    in een range van -10000, 10000 met i == range(-10000, 10000):
        als i groter is dan of gelijk is aan het getal (real):
            JA: geef int(i) terug
        als getal (real) == 0:
            JA: geef 0 terug
        anders verhogen we i met 1
    """
    for i in range(-10000, 10000):
        if i >= real:
            return int(i)
        elif real == 0:
            return 0
        else:
            i = i + 1

    """
    if real == int(real):
        return int(real)
    return int(real // 1 + 1)
    
    # Vereenvoudiging met operator; hetzelfde resultaat gerealiseerd
    """


def div(n):
    """
    Bepaal alle delers van een geheel getal.

    Het positieve gehele getal a is een deler van n, als er een positief geheel getal b is, zodat a × b = n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle delers van `n`.
    """
    """
    Maak nieuwe lijst aan met doel om te retourneren (divisors)
    voor deler in range 1 en n + 1 (delen door 0 kan niet en (n + 1) voor rangebehoud):
        als getal (n) deelbaar is door deler uit for loop met restwaarde 0:
            voeg deler toe aan lijst divisors
    indien range voltooid, return lijst met delers
    """
    divisors = []
    for deler in range(1, (n + 1)):
        if n % deler == 0 and deler != 0:
            divisors.append(deler)
    return sorted(divisors)


def is_prime(n):
    """
    Bepaal of gegeven getal een priemgetal is.

    Hint: maak gebruik van de functie `div()`.
    Optioneel: bedenk een efficiënter alternatief.

    Args:
        n (int): Een geheel getal.

    Returns:
        bool: True als het getal een priemgetal is, anders False.
    """
    """
    als priem groter is dan 1 (priem kan niet negatief zijn en mag niet 1 zijn)
    EN als de lijstgrootte gelijk is aan 2 (1 en getal zelf):
        True: getal is priemgetal
    anders
        False: getal is negatief, is 1 of geen priemgetal
    """
    if n > 1 and len(div(n)) == 2:
        return True
    else:
        return False


def primes(num):
    """
    Bepaal alle priemgetallen kleiner dan een bepaald geheel getal.

    Hint: Maak gebruik van de functie `is_prime()`.

    Args:
        num (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemgetallen kleiner dan `num`.
    """
    """
    maak nieuwe lijst aan (primelist)
    voor getal in range 0 en groot getal:
        als getal priem is EN getal kleiner is dan groot getal EN getal niet 1 is:
            voeg getal toe aan lijst
    return lijst met priemgetallen voor gegeven groot getal 
    """
    primelist = []
    for getal in range(0, num):
        if is_prime(getal) and getal <= num and getal != 1:
            primelist.append(getal)
    return sorted(primelist)


def primefactors(n):
    """
    Bepaal de verzameling van priemfactoren van n.

    Args:
        n (int): Een geheel getal.

    Returns:
        list: Een gesorteerde lijst met alle priemfactoren van n. Als n kleiner
            dan 2, retourneer dan een lege lijst `[]`.
    """
    """
    maak nieuwe lijst (factors)
    voor elke factor in f(primes(n+1)):
        zolang factor groter is dan 1 EN groot getal deelbaar is door factor met restwaarde 0:
            voeg factor toe aan lijst
            nieuw groot getal = oud groot getal delen door factor
    lijst met factoren wordt teruggegeven na elke loop
    """
    factors = []
    for factor in primes(n + 1):
        while factor > 1 and n % factor == 0:
            factors.append(int(factor))
            n /= factor
    return sorted(factors)


def gcd(a, b):
    """
    Bepaal de grootste grootste gemene deler (ook wel 'greatest common divisor', gcd) van twee natuurlijke getallen.

    Je hebt twee opties voor deze opgave:
    1.  Je programmeert hier het algoritme van Euclides.
        Zie: https://nl.wikipedia.org/wiki/Algoritme_van_Euclides
    2.  Je bedenkt zelf een oplossing waarbij je gebruik maakt van de eerder
        geschreven methode div(n) om de gcd te bepalen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: De grootste grootste gemene deler.
    """
    """
    Dit is het algoritme van Euclides:
    
    zolang a niet gelijk is aan b:
        als a groter is dan b:
            nieuwe waarde a = oude a - b
            als a gelijk is aan b:
                geef b terug
        anders als a kleiner is dan b:
            nieuwe waarde b is oude b - a
        anders als b gelijk is aan 0:
            geef b terug
    wanneer a gelijk staat aan b, geef b terug.
    """
    while a != b:
        if a > b:
            a -= b
            if a == 0:
                return b
        elif a < b:
            b -= a
        elif b == 0:
            return b
    return b


def lcm(a, b):
    """
    Bepaal het kleinste gemene veelvoud, kgv (ook wel 'least common multiple', lcm) van twee natuurlijke getallen.

    Args:
        a (int): Een geheel getal.
        b (int): Een geheel getal.

    Returns:
        int: Het kleinste gemene veelvoud.
    """
    """
    lcm(a, b) is het tegenovergestelde van gcd(a, b)
    """

    """
    # met conversieformule
    ar = a  # Startwaarden opslaan
    br = b  # Startwaarden opslaan
    while a != b:  # gcd bepalen (a.d.h.v. de gcd functie)
        if a > b:
            a = a - b
            if a == 0:
                break
        elif a < b:
            b = b - a
        elif b == 0:
            break
    return int((ar * br) / b)  # de omzetformule gebruikt gcd(a, b) ipv b, want gcd(a, b) wordt vervangen met b
    """
    return int((a * b) / gcd(a, b))  # omzetten d.m.v. de formule volgens les 1; laatste dia


def add_frac(n1, d1, n2, d2):
    """Sommeer twee breuken als breuk. Vereenvoudig de breuk zover als mogelijk.

    Args:
        n1 (int): De teller van de eerste breuk.
        d1 (int): De noemer van de eerste breuk.
        n2 (int): De teller van de tweede breuk.
        d2 (int): De noemer van de tweede breuk.

    Returns:
        tuple: De som *als breuk*, met eerst de teller en dan de noemer van het resultaat.

    Examples:
        Gegeven 1/3 + 1/5 = 8/15, dan

        >> add_frac(1, 3, 1, 5)
        (8, 15)

        Gegeven 1/2 + 1/4 = 3/4, dan

        >> add_frac(1, 2, 1, 4)
        (3, 4)

        Gegeven 2/3 + 3/2 = 13/6, dan

        >> add_frac(2, 3, 3, 2)
        (13, 6)
    """

    """
    Maak nieuwe lijst aan
    in range 2 en noemer resultaat + 2:
        Voeg getal toe aan lijst
        
    Draai lijst om voor deling met grootste getal eerst
    Voor elke deler binnen lijst deler:
        Zolang noemer resultaat gedeeld door deler restwaarde 0 heeft EN opsomming resultaat gedeeld door deler restwaarde 0 heeft
            deel resultaat door mogelijke deler
            
    geef resultaat terug in vorm van tuple
    """

    resd = d1 * d2  # deler resultaat
    noe1 = n1 * d2  # vermenigvuldiging compatibiliteit noemer 1
    noe2 = n2 * d1  # vermenigvuldiging compatibiliteit noemer 2

    delers = []
    for n in range(2, resd + 2):
        delers.append(n)
    delers.reverse()

    for x in delers:
        while resd % x == 0 and int(noe1 + noe2) % x == 0:
            resd /= x
            noe1 /= x
            noe2 /= x

    return int(noe1 + noe2), int(resd)


"""
==========================[ HU TESTRAAMWERK ]================================
Onderstaand staan de tests voor je code -- hieronder mag je niets wijzigen!
Je kunt je code testen door deze file te runnen of met behulp van pytest.
"""


def __my_assert_args(function, args, expected_output, check_type=True):
    """
    Controleer of gegeven functie met gegeven argumenten het verwachte resultaat oplevert.

    Optioneel wordt ook het return-type gecontroleerd.
    """
    argstr = str(args).replace(',)', ')')
    output = function(*args)

    # Controleer eerst het return-type (optioneel)
    if check_type:
        msg = f"Fout: {function.__name__}{argstr} geeft geen {type(expected_output)} terug als return-type"
        assert type(output) is type(expected_output), msg

    # Controleer of de functie-uitvoer overeenkomt met de gewenste uitvoer
    msg = f"Fout: {function.__name__}{argstr} geeft {output} in plaats van {expected_output}"
    if type(expected_output) is float:
        # Vergelijk bij float als return-type op 7 decimalen om afrondingsfouten te omzeilen
        assert round(output - expected_output, 7) == 0, msg
    else:
        assert output == expected_output, msg


def test_id():
    assert naam != "", "Je moet je naam nog invullen!"
    assert studentnummer != -1, "Je moet je studentnummer nog invullen!"
    assert klas != "", "Je moet je klas nog invullen!"


def test_is_even():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), False),
        ((4,), True)
    ]

    for case in testcases:
        __my_assert_args(is_even, case[0], case[1])


def test_floor():
    testcases = [
        ((1.05,), 1),
        ((1.95,), 1),
        ((-1.05,), -2),
        ((-1.95,), -2),
        ((0.05,), 0),
        ((-0.05,), -1),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(floor, case[0], case[1])


def test_floor_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(floor, (x,), math.floor(x))


def test_ceil():
    testcases = [
        ((1.05,), 2),
        ((1.95,), 2),
        ((-1.05,), -1),
        ((-1.95,), -1),
        ((0.05,), 1),
        ((-0.05,), 0),
        ((0.0,), 0),
        ((1.0,), 1),
        ((-1.0,), -1)
    ]

    for case in testcases:
        __my_assert_args(ceil, case[0], case[1])


def test_ceil_simulated():
    import random
    import math

    for _ in range(10):
        x = random.uniform(-10.0, 10.0)
        __my_assert_args(ceil, (x,), math.ceil(x))


def test_div():
    testcases = [
        ((1,), [1]),
        ((2,), [1, 2]),
        ((3,), [1, 3]),
        ((4,), [1, 2, 4]),
        ((8,), [1, 2, 4, 8]),
        ((12,), [1, 2, 3, 4, 6, 12]),
        ((19,), [1, 19]),
        ((25,), [1, 5, 25]),
        ((929,), [1, 929]),
        ((936,), [1, 2, 3, 4, 6, 8, 9, 12, 13, 18, 24, 26, 36, 39, 52, 72, 78, 104, 117, 156, 234, 312, 468, 936])
    ]

    for case in testcases:
        __my_assert_args(div, case[0], sorted(case[1]))


def test_is_prime():
    testcases = [
        ((1,), False),
        ((2,), True),
        ((3,), True),
        ((4,), False),
        ((5,), True),
        ((6,), False),
        ((9,), False),
        ((29,), True)
    ]

    for case in testcases:
        __my_assert_args(is_prime, case[0], case[1])


def test_primefactors():
    testcases = [
        ((-1,), []),
        ((1,), []),
        ((2,), [2]),
        ((3,), [3]),
        ((4,), [2, 2]),
        ((8,), [2, 2, 2]),
        ((12,), [2, 2, 3]),
        ((2352,), [2, 2, 2, 2, 3, 7, 7]),
        ((9075,), [3, 5, 5, 11, 11])
    ]

    for case in testcases:
        __my_assert_args(primefactors, case[0], sorted(case[1]))


def test_primes():
    testcases = [
        ((1,), []),
        ((2,), []),
        ((3,), [2]),
        ((4,), [2, 3]),
        ((5,), [2, 3]),
        ((6,), [2, 3, 5]),
        ((30,), [2, 3, 5, 7, 11, 13, 17, 19, 23, 29])
    ]

    for case in testcases:
        __my_assert_args(primes, case[0], sorted(case[1]))


def test_gcd():
    testcases = [
        ((60, 1), 1),
        ((60, 6), 6),
        ((60, 7), 1),
        ((60, 8), 4),
        ((60, 9), 3),
        ((60, 11), 1),
        ((60, 13), 1),
        ((60, 14), 2),
        ((60, 15), 15),
        ((60, 16), 4),
        ((60, 18), 6)
    ]

    for case in testcases:
        __my_assert_args(gcd, case[0], case[1])


def test_gcd_simulated():
    import random
    import math

    for _ in range(10):
        a = random.randrange(3, 201, 3)
        b = random.randrange(4, 201, 4)
        __my_assert_args(gcd, (a, b), math.gcd(a, b))


def test_lcm():
    testcases = [
        ((60, 1), 60),
        ((60, 2), 60),
        ((60, 7), 420),
        ((60, 8), 120),
        ((60, 9), 180),
        ((60, 10), 60),
        ((60, 11), 660),
        ((60, 18), 180)
    ]

    for case in testcases:
        __my_assert_args(lcm, case[0], case[1])


def test_add_frac():
    testcases = [
        ((1, 3, 1, 5), (8, 15)),
        ((1, 2, 1, 4), (3, 4)),
        ((2, 3, 3, 2), (13, 6)),
        ((1, 2, 1, 6), (2, 3)),
        ((3, 4, 1, 6), (11, 12)),
        ((1, 6, 3, 4), (11, 12)),
        ((1, 2, 1, 3), (5, 6)),
        ((1, 2, 2, 3), (7, 6))
    ]

    for case in testcases:
        __my_assert_args(add_frac, case[0], case[1])


def __main():
    """ Test alle functies. """
    # Noodzakelijk voor gekleurde tekst binnen een Windows terminal
    import os
    os.system("")

    try:
        print("\x1b[32m")  # Groene tekstkleur
        test_id()

        test_is_even()
        print("Je functie is_even(n) werkt goed!")

        test_floor()
        test_floor_simulated()
        print("Je functie floor(real) werkt goed!")

        test_ceil()
        test_ceil_simulated()
        print("Je functie ceil(real) werkt goed!")

        test_div()
        print("Je functie div(n) werkt goed!")

        test_is_prime()
        print("Je functie is_prime(n) werkt goed!")

        test_primes()
        print("Je functie primes(num) werkt goed!")

        test_primefactors()
        print("Je functie primefactors(n) werkt goed!")

        test_gcd()
        test_gcd_simulated()
        print("Je functie gcd(a, b) werkt goed!")

        test_lcm()
        print("Je functie lcm(a, b) werkt goed!")

        test_add_frac()
        print("Je functie add_frac(n1, d1, n2, d2) werkt goed!")

        print("\nGefeliciteerd, alles lijkt te werken!")
        print("Lever je werk nu in op Canvas...")


    except AssertionError as ae:
        print("\x1b[31m")  # Rode tekstkleur
        print(ae)

    print("\x1b[0m")  # Reset tekstkleur


if __name__ == '__main__':
    __main()