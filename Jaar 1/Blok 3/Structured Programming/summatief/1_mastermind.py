from random import *
from time import perf_counter
import time


def conversie():  # DONE
    translatie = {
        '1': 'rood',
        '2': 'oranje',
        '3': 'geel',
        '4': 'groen',
        '5': 'blauw',
        '6': 'wit',
        '7': 'bruin',
        '8': 'zwart'
    }
    return translatie


def reeks():  # DONE
    reeks_dict = [choice(range(1, 8)) for x in range(int(4))]
    return reeks_dict


def nakijken(antwoorden_lst, keuze_lst):
    zwart = wit = 0
    not_index = []
    for x in range(len(keuze_lst)):  # Eerst kijken voor 'goed'
        if antwoorden_lst[x] == keuze_lst[x]:
            zwart += 1
            not_index.append(keuze_lst[x])
    for x in range(len(keuze_lst)):  # Dan kijken voor 'andere plaats' zonder rekening te houden voor 'goed'
        if (keuze_lst[x] in antwoorden_lst) and (keuze_lst[x] not in not_index):
            wit += 1
    return {'zwart': zwart, 'wit': wit}


def bord():
    pass


def simple_algorithm(antwoord):
    gekozen = [x for x in range(len(conversie()) + 1) if x != 0]
    not_list = []
    for keuze_1 in gekozen:
        if keuze_1 not in not_list:
            for keuze_2 in gekozen:
                if keuze_2 not in not_list:
                    for keuze_3 in gekozen:
                        if keuze_3 not in not_list:
                            for keuze_4 in gekozen:
                                if keuze_4 not in not_list:
                                    beoordeling = nakijken(antwoord, [keuze_1, keuze_2, keuze_3, keuze_4])
                                    if beoordeling['zwart'] == 4:
                                        return keuze_1, keuze_2, keuze_3, keuze_4
                                    elif beoordeling['wit'] == beoordeling['zwart'] == 0 and keuze_4 not in not_list:
                                        not_list.append(keuze_4)

    # TODO: Modify | Kijk naar beoordeling en haal waarden weg waarvan zeker is dat deze niet vaker voorkomen
    pass


def complex_algorithm(antwoord):
    # TODO: ADD | Een Gevonden ingewikkelde algoritme (mag uit Artikel van Uni Groningen)
    # print(antwoord)
    # print(reeks())
    return None


def made_algorithm(antwoord):
    # TODO: ADD | Zelfgemaakte algoritme
    return None


def initialize(antwoord):
    # vraag = ['geel', 'wit', 'bruin', 'wit']
    # antwoord = ['groen', 'rood', 'groen', 'wit']
    start = perf_counter()
    print(f'\x1b[32m\nCorrecte Combinatie: \x1b[31m{antwoord}')
    print(f'\x1b[32mSimple Teruggegeven: \x1b[31m{simple_algorithm(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')
    print(f'\x1b[32mComplex Teruggegeven: \x1b[31m{complex_algorithm(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{made_algorithm(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


if __name__ == '__main__':
    for c in range(20000 + 1):
        def_antwoord = reeks()  # ['wit', 'geel', 'geel', 'bruin']
        print(f'\n\x1b[31m{c}\x1b[32m')
        initialize(def_antwoord)
