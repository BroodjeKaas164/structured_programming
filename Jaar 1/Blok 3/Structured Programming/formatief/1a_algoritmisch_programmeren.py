import random


# ===================[Opdracht 1 : Piramide]===================
def piramide_for(height):  # DONE
    for x in range(0, height + 1, 1):
        print(x * '*')
    for x in range(height - 1, 0, -1):
        print(x * '*')


def piramide_while(height):  # DONE
    x = 0
    while x < height:
        print(x * '*')
        x += 1
    while x > 0:
        print(x * '*')
        x -= 1


# ===================[Opdracht 2 : Tekstcheck]===================
def tekstcheck(string_reeks_1, string_reeks_2):  # DONE
    str_index = 0
    for str_index in range(len(string_reeks_1)):
        if string_reeks_1 == string_reeks_2:
            print('De opgegeven waarden zijn hetzelfde!')
            break
        if string_reeks_1[str_index] == string_reeks_2[str_index]:
            pass
        else:
            print(f'Het eerste verschil zit op index: {str_index}!')
            break


# ===================[Opdracht 3 : Lijst Check]===================
def count(lst, target):  # DONE
    return len([getal for getal in lst if getal == target])


def next_difference(lst):  # DONE
    return max([lst[x] - lst[x - 1] for x in range(len(lst))])


def een_nul(lst):  # DONE
    aantal_nul, aantal_een = count(lst, 0), count(lst, 1)
    print(f'\t\t\t\t\t\t\t\t\t\t\t\t\taantal 0: {aantal_nul}, aantal 1: {aantal_een}')
    if (aantal_een > aantal_nul) and (aantal_nul <= 12):
        return True
    else:
        return False


# ===================[Opdracht 4 : Palindroom]===================
def palindroom(woord):  # DONE | De manier van recursie ©D. Tjon-A-Njoek --- 2021-21-12
    if len(woord) <= 1:
        return True
    else:
        return woord[0] == woord[-1] and palindroom((woord[1:-1]))


# ===================[Opdracht 5 : Sorteren]===================
def sorteren(lst):  # DONE
    def swap(lst, index1, index2):
        lst[index1], lst[index2] = lst[index2], lst[index1]

    def find_index_of_minimum(lst, start_index=0):
        minimum = lst[start_index]
        index_of_minimum = start_index

        for cursor in range(start_index, len(lst)):
            if lst[cursor] < minimum:
                minimum = lst[cursor]
                index_of_minimum = cursor

        return index_of_minimum

    lst_sorted = lst.copy()
    for index in range(len(lst_sorted)):
        index_of_minimum = find_index_of_minimum(lst_sorted, index)
        swap(lst_sorted, index, index_of_minimum)

    return lst_sorted


# ===================[Opdracht 6 : Gemiddelde Berekenen]===================
def gemiddelde_in_lijst(lst):  # DONE
    totaal = 0
    return sum([totaal + getal for getal in lst]) / len(lst)


def gemiddelde_per_lijst(lst):  # DONE
    totaal = 0
    return sum([totaal + gemiddelde_in_lijst(sub_lst) for sub_lst in lst]) / len(lst)


# ===================[Opdracht 7 : Random]===================
def random_guess(geheim):  # DONE
    keuze = ''
    while keuze != geheim:
        keuze = int(input('\x1b[32m7: Random | Geef een cijfer op: >>> \x1b[31m'))
        if keuze == geheim:  # voor prettyprint in geval van herhaalde input cases
            break


# ===================[Opdracht 8 : Compressie]===================
def compressie():
    # TODO: Add | Functie Compressie
    pass


# ===================[Opdracht 9 : Cyclisch Verschuiven]===================
def cyclisch_verschuiven(ch, n):
    assigned_binary = bin(ord(ch))[2:]  # ©https://www.educative.io/edpresso/how-to-convert-string-to-binary-in-python
    for stap in range(abs(n)):
        if n > 0:
            assigned_binary += assigned_binary[:1]
            assigned_binary = assigned_binary[1:]
            print(assigned_binary)
        if n < 0:
            assigned_binary = assigned_binary[-1:] + assigned_binary
            assigned_binary = assigned_binary[:-1]
            print(assigned_binary)


# ===================[Opdracht 10 : Fibonacci]===================
def fibonacci(lengte_lst, reeks):
    if len(reeks) < lengte_lst:
        reeks.append(reeks[-1] + reeks[-2])
        return fibonacci(lengte_lst, reeks)
    elif len(reeks) == lengte_lst:
        return reeks


# ===================[Opdracht 11 : Caesar Cijfers]===================
def caesar_cijfers():
    # TODO: Add | Functie caesar_cijfer
    pass


# ===================[Opdracht 12 : FizzBuzz]===================
def fizzbuzz():  # DONE | Hardcode-Manier, daarmee met hoge kans ook de slechtste manier
    for x in range(1, 101, 1):
        if x % 3 == 0 and x % 5 == 0:
            print(f'{x} | fizzbuzz')
        elif x % 3 == 0:
            print(f'{x} | fizz')
        elif x % 5 == 0:
            print(f'{x} | buzz')
        else:
            print(f'{x} | {x}')


"""
=================================[Test]=================================
Hieronder test ik de functies.

Echter is dit proces niet volledig geautomatiseerd vanwege het vereiste
dat dit gebruikersinput nodig heeft.

Aangeroepen functies die gecommenteerd zijn, zijn niet uitgewerkt... 😔
"""


def test_algoritmisch_programmeren():
    # ===================[Opdracht 1 : Piramide]===================
    input_lengte = input('\n\x1b[32m1: Piramide (For) | Hoe lang is de piramide? >>> \x1b[31m')
    piramide_for(int(input_lengte))

    input_lengte = input('\n\x1b[32m1: Piramide (While) | Hoe lang is de piramide? >>> \x1b[31m')
    piramide_for(int(input_lengte))

    # ===================[Opdracht 2 : Tekstcheck]===================
    str_1, str_2 = input('\n\x1b[32m2: Tekstcheck | Geef een String 1: >>> '), input('\x1b[32m2: Tekstcheck | Geef een String 2: >>> ')
    tekstcheck(str_1, str_2)

    # ===================[Opdracht 3 : Lijst check]===================
    test_lst_count = [random.choice(range(0, 11)) for x in range(10)]
    test_target = random.randint(0, 10)
    print(f'\n\x1b[32m3: Count | Willekeurige lijst: \x1b[31m{test_lst_count}')
    print(f'\x1b[32m3: Count | Willekeurige Target: \x1b[31m{test_target}')
    print(f'\x1b[32m3: Count | Frequentie in lijst: \x1b[31m{count(test_lst_count, test_target)}')

    print(f'\n\x1b[32m3: Grootste Verschil | \x1b[31m{next_difference(test_lst_count)}')

    for x in range(3):
        test_lst_nee = [random.choice(range(0, 2)) for x in range(15)]
        print(f'\n\x1b[32m3: Nullen en Enen | Serie \x1b[31m{x + 1}\x1b[32m | Willekeurige lijst: \x1b[31m{test_lst_nee}')
        print(f'\x1b[32m3: Nullen en Enen | Serie \x1b[31m{x + 1}\x1b[32m | Voldoet aan eisen? \x1b[31m{een_nul(test_lst_nee)}')

    # ===================[Opdracht 4 : Palindroom]===================
    test_woord = input('\n\x1b[32m4: Palindroom | Voer een woord in: >>>:\x1b[31m')
    print(f'\x1b[32m4: Palindroom | \x1b[31m{test_woord}')
    state = palindroom(test_woord.lower())
    if state:
        print(f'\x1b[32m4: Palindroom | \x1b[31m{test_woord} is een palindroom!')
    elif not state:
        print(f'\x1b[32m4: Palindroom | \x1b[31m{test_woord} is helaas geen palindroom...')

    # ===================[Opdracht 5 : Sorteren]===================
    test_lst_sort = [random.choice(range(0, 101)) for x in range(40)]
    print(f'\n\x1b[32m5: Sorteren | Willekeurige lijst: \x1b[31m{test_lst_sort}')
    print(f'\x1b[32m5: Sorteren | Gesorteerde lijst: \x1b[31m{sorteren(test_lst_sort)}\x1b[32m | Insertion Sort ©D. Tjon-A-Njoek --- 2021-14-12')

    # ===================[Opdracht 6 : Gemiddelde Berekenen]===================
    test_lst_gem_in = [random.choice(range(0, 101)) for x in range(25)]
    print(f'\n\x1b[32m6: Gemiddelde Berekenen in lijst | Lijst: \x1b[31m{test_lst_gem_in}')
    print(f'\x1b[32m6: Gemiddelde Berekenen in lijst | Gemiddelde \x1b[31m{gemiddelde_in_lijst(test_lst_gem_in)}')

    test_lst_gem_per = [[random.choice(range(0, 101)) for x in range(random.choice(range(2, 11)))] for x in range(random.choice(range(3, 11)))]
    print(f'\n\x1b[32m6: Gemiddelde Berekenen per lijst | Lijst: \x1b[31m{test_lst_gem_per}')
    print(f'\x1b[32m6: Gemiddelde Berekenen per lijst | Gemiddelde \x1b[31m{gemiddelde_per_lijst(test_lst_gem_per)}')

    # ===================[Opdracht 7 : Random]===================
    geheim = random.randint(1, 10)
    print(f'\n\x1b[32m7: Random | Antwoord: \x1b[31m{geheim}')
    random_guess(geheim)

    # ===================[Opdracht 8 : Compressie]===================
    # compressie()

    # ===================[Opdracht 9 : Cyclisch Verschuiven]===================
    character = input('\n\x1b[32m9: Cyclisch Verschuiven | Character: Geef een Letter: >>> \x1b[31m')
    verschuiving = input('\x1b[32m9: Cyclisch Verschuiven | Character: Geef verschuiving op: >>> \x1b[31m')
    print(f'\x1b[32m9: Cyclisch Verschuiven | Character: \x1b[31m{character}')
    print(f'\x1b[32m9: Cyclisch Verschuiven | Verschuiving: \x1b[31m{verschuiving}')
    cyclisch_verschuiven(character, int(verschuiving))

    # ===================[Opdracht 10 : Fibonacci]===================
    test_input_fib = input('\n\x1b[32m10: Fibonacci | Hoe lang moet de reeks zijn? >>> \x1b[31m')
    print(f'\x1b[32m10: Fibonacci | Reeks \x1b[31m{fibonacci(int(test_input_fib), [0, 1])}')

    # ===================[Opdracht 11 : Caesar Cijfers]===================
    # caesar_cijfers()

    # ===================[Opdracht 12 : FizzBuzz]===================
    print(f'\n\x1b[32m12: FizzBuzz | Reeks:\x1b[31m')
    fizzbuzz()


if __name__ == '__main__':
    test_algoritmisch_programmeren()
