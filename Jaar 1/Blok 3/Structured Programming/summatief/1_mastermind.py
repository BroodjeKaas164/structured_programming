from random import *
from time import perf_counter
import time


def _dict_conversie():  # DONE
    translatie = {
        '1': 'Rood',
        '2': 'Oranje',
        '3': 'Geel',
        '4': 'Groen',
        '5': 'Blauw',
        '6': 'Wit',
        '7': 'Bruin',
        '8': 'Zwart'
    }
    return translatie


def _conversie(getal, translate_dict):  # DONE
    return translate_dict[str(getal)]


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


def algorithm_simple(antwoord):
    gekozen = [x for x in range(len(_dict_conversie()) + 1) if x != 0]
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
                                        return _conversie(keuze_1, _dict_conversie()), _conversie(keuze_2, _dict_conversie()), _conversie(keuze_3, _dict_conversie()), _conversie(keuze_4, _dict_conversie())
                                    elif beoordeling['wit'] == beoordeling['zwart'] == 0 and keuze_4 not in not_list:
                                        not_list.append(keuze_4)

    # TODO: Modify | Kijk naar beoordeling en haal waarden weg waarvan zeker is dat deze niet vaker voorkomen
    # TODO: ADD | Schaalbaar?
    pass


def algorithm_complex(antwoord):
    # TODO: ADD | Een Gevonden ingewikkelde algoritme (mag uit Artikel van Uni Groningen)
    # print(antwoord)
    # print(reeks())
    return None


def algorithm_made(antwoord):
    # TODO: ADD | Zelfgemaakte algoritme
    return None


def initialize(antwoord):
    # vraag = ['geel', 'wit', 'bruin', 'wit']
    # antwoord = ['groen', 'rood', 'groen', 'wit']
    antwoord_str = [_conversie(x, _dict_conversie()) for x in antwoord]
    print(f'\x1b[32m\033[1mCorrecte Combinatie: \033[0m\x1b[31m{antwoord_str}')

    start = perf_counter()
    print(f'\x1b[32mSimple Teruggegeven: \x1b[31m{algorithm_simple(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mComplex Teruggegeven: \x1b[31m{algorithm_complex(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{algorithm_made(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


if __name__ == '__main__':
    for c in range(50000 + 1):
        print(f'\n\x1b[32m\033[1mSpelnummer: \033[0m\x1b[31m{c}\x1b[32m')
        def_antwoord = reeks()  # ['wit', 'geel', 'geel', 'bruin']
        initialize(def_antwoord)
