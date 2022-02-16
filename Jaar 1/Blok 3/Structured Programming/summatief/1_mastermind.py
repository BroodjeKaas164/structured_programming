from random import *
from time import perf_counter
import time
import itertools


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
    try:
        return translate_dict[str(getal)]
    except KeyError as ke:
        pass


def reeks():  # DONE
    reeks_dict = [choice(range(1, 8)) for x in range(int(4))]
    return reeks_dict


def nakijken(antwoorden_lst, keuze_lst):  # DONE
    zwart = wit = 0
    not_index = []
    for x in range(len(keuze_lst)):  # Eerst kijken voor 'goed'
        if antwoorden_lst[x] == keuze_lst[x]:
            zwart += 1
            not_index.append(keuze_lst[x])
    for x in range(len(keuze_lst)):  # Dan kijken voor 'andere plaats' zonder rekening te houden voor 'goed'
        if (keuze_lst[x] in antwoorden_lst) and (keuze_lst[x] not in not_index):
            wit += 1

    # TODO: MODIFY | In gevallen antw=[x, x, x, y] en kze=[y, x, x, x] geeft {zwart:2, wit:1} --> Moet zijn {zwart:2, wit:2}
    return {'zwart': zwart, 'wit': wit}


def algorithm_user(antwoord):
    # TODO: ADD | Gebruiker tegen Computer
    antwoord_str = [_conversie(c, _dict_conversie()) for c in antwoord]
    tries_int = 0
    tries = []
    tries_str = []
    tries_secret = []

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    while True:
        keuzes = []
        print(f'\x1b[32m{_dict_conversie()}')
        try:
            print(f'\x1b[32mAntwoord: >>> \x1b[31m{antwoord}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m')
            keuze_1 = input('\n\x1b[32mkeuze 1: >>> \x1b[31m')
            keuze_2 = input('\x1b[32mkeuze 2: >>> \x1b[31m')
            keuze_3 = input('\x1b[32mkeuze 3: >>> \x1b[31m')
            keuze_4 = input('\x1b[32mkeuze 4: >>> \x1b[31m')

            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            keuzes = [int(keuze_1), int(keuze_2), int(keuze_3), int(keuze_4)]
            keuzes_str = [_conversie(keuze_1, _dict_conversie()), _conversie(keuze_2, _dict_conversie()), _conversie(keuze_3, _dict_conversie()), _conversie(keuze_4, _dict_conversie())]

            tries.append(keuzes)

            zwart, wit = nakijken(antwoord, keuzes)['zwart'], nakijken(antwoord, keuzes)['wit']
            tries_secret.append(f'Goed: {zwart}, Anders: {wit}')
            tries_str.append(keuzes_str)

            if keuzes == antwoord:
                break
            elif keuzes != antwoord:
                tries_int += 1
                for combination in range(len(tries_str)):
                    print(f'\x1b[31m{combination + 1}\x1b[32m | \x1b[31m{tries[combination]}\x1b[32m | \x1b[31m{tries_str[combination]}\x1b[32m | \x1b[31m{tries_secret[combination]}\x1b[32m')

        except ValueError as ve:
            pass

    return keuzes


def algorithm_simple(antwoord):
    gekozen = [x for x in range(len(_dict_conversie()) + 1) if x != 0]
    combinations = []
    setnumber = 0
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
                                    setnumber += 1
                                    combinations.append(f'{setnumber} | {[keuze_1, keuze_2, keuze_3, keuze_4]}')
                                    if beoordeling['zwart'] == 4:
                                        print(f'\x1b[32mGebruikte Combinaties | \x1b[31m{combinations}\x1b[32m')
                                        return _conversie(keuze_1, _dict_conversie()), _conversie(keuze_2, _dict_conversie()), _conversie(keuze_3, _dict_conversie()), _conversie(keuze_4, _dict_conversie())
                                    elif beoordeling['wit'] == beoordeling['zwart'] == 0 and keuze_4 not in not_list:
                                        not_list.append(keuze_4)

    # TODO: MODIFY | Kijk naar beoordeling en haal waarden weg waarvan zeker is dat deze niet vaker voorkomen
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


def initialize_cpu_cpu(antwoord):
    # vraag = ['geel', 'wit', 'bruin', 'wit']
    # antwoord = ['groen', 'rood', 'groen', 'wit']
    antwoord_str = [_conversie(x, _dict_conversie()) for x in antwoord]
    print(f'\x1b[32m\033[1mCorrecte Combinatie Int: \033[0m\x1b[31m{antwoord}')
    print(f'\x1b[32m\033[1mCorrecte Combinatie Str: \033[0m\x1b[31m{antwoord_str}')

    start = perf_counter()
    print(f'\x1b[32mSimple Teruggegeven: \x1b[31m{algorithm_simple(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mComplex Teruggegeven: \x1b[31m{algorithm_complex(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{algorithm_made(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


def initialize_user_cpu(antwoord):
    start = perf_counter()
    antwoord_str = [_conversie(x, _dict_conversie()) for x in antwoord]
    print(f'\x1b[32mUser Teruggegeven: \x1b[31m{algorithm_user(antwoord)}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m in \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


if __name__ == '__main__':
    state = input(f'\n\n\n\n\x1b[32mPlay or Watch? \x1b[31m(P/W)\x1b[32m: >>> \x1b[31m').lower()

    if state == 'w':
        for c in range(20000 + 1):
            print(f'\n\x1b[32m\033[1mSpelnummer: \033[0m\x1b[31m{c}\x1b[32m')
            def_antwoord = reeks()
            initialize_cpu_cpu(def_antwoord)

    elif state == 'p':
        def_antwoord = reeks()
        initialize_user_cpu(def_antwoord)
