from time import perf_counter
import itertools
from mastermind_utilities import *


def algorithm_user(antwoord, game_size):
    # TODO: ADD | Gebruiker tegen Computer
    antwoord_str = [conversie(x) for x in antwoord]
    tries_int = 0
    tries = []
    tries_str = []
    tries_secret = []

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    while True:
        keuzes = []
        print(f'\x1b[32m{dict_conversie()}')
        try:
            print(f'\x1b[32mAntwoord: >>> \x1b[31m{antwoord}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m')
            while True:
                keuze_1 = input('\n\x1b[32mkeuze 1: >>> \x1b[31m')
                keuze_2 = input('\x1b[32mkeuze 2: >>> \x1b[31m')
                keuze_3 = input('\x1b[32mkeuze 3: >>> \x1b[31m')
                keuze_4 = input('\x1b[32mkeuze 4: >>> \x1b[31m')
                if 0 < int(keuze_1) < (len(dict_conversie()) + 1) and 0 < int(keuze_2) < (len(dict_conversie()) + 1) and 0 < int(keuze_3) < (len(dict_conversie()) + 1) and 0 < int(keuze_4) < (len(dict_conversie()) + 1):
                    break
                else:
                    print('\x1b[31mIncorrecte invoer\x1b[32m')
            print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')

            keuzes = [int(keuze_1), int(keuze_2), int(keuze_3), int(keuze_4)]
            keuzes_str = [conversie(keuze_1), conversie(keuze_2), conversie(keuze_3), conversie(keuze_4)]

            zwart, wit = nakijken(antwoord, keuzes)['zwart'], nakijken(antwoord, keuzes)['wit']
            tries.append(keuzes)
            tries_secret.append(f'Goed: {zwart}, Anders: {wit}')
            tries_str.append(keuzes_str)

            if keuzes == antwoord:
                break
            elif keuzes != antwoord:
                # TODO: MODIFY | index range buiten dictionary van kleuren wordt alsnog toegevoegd aan de lijst met pogingen
                tries_int += 1
                for combination in range(len(tries_str)):
                    print(f'\x1b[31m{combination + 1}\x1b[32m | \x1b[31m{tries[combination]}\x1b[32m | \x1b[31m{tries_str[combination]}\x1b[32m | \x1b[31m{tries_secret[combination]}\x1b[32m')
            if tries_int >= game_size:
                print('\n\x1b[31mHow Unfortunate...\x1b[32m')
                print(f'\x1b[32mAntwoord: \x1b[31m{antwoord}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m')
                break
        except ValueError as ve:
            pass
    return keuzes


def algorithm_simple(antwoord):
    """
    De Simple Algorithm uit het Artikel van Universiteit Groningen.
    :param antwoord: de geheime combinatie waarnaar gewerkt moet worden.
    :return: tuple met resultaatwaarden die gelijkstaan aan het antwoord
    """
    opties = [x for x in range(len(dict_conversie()) + 1) if x != 0]
    combinations = []
    setnumber = 0
    not_list = []
    for keuze_1 in opties:
        if keuze_1 not in not_list:
            for keuze_2 in opties:
                if keuze_2 not in not_list:
                    for keuze_3 in opties:
                        if keuze_3 not in not_list:
                            for keuze_4 in opties:
                                if keuze_4 not in not_list:
                                    beoordeling = nakijken(antwoord, [keuze_1, keuze_2, keuze_3, keuze_4])
                                    setnumber += 1
                                    combinations.append([keuze_1, keuze_2, keuze_3, keuze_4])
                                    if beoordeling['zwart'] == 4:
                                        # print(f'\x1b[32mGebruikte Combinaties | \x1b[31m{combinations}\x1b[32m')
                                        return conversie(keuze_1), conversie(keuze_2), conversie(keuze_3), conversie(keuze_4)
                                    elif beoordeling['wit'] == beoordeling['zwart'] == 0 and keuze_4 not in not_list:
                                        not_list.append(keuze_4)

    # TODO: MODIFY | Kijk naar beoordeling en haal waarden weg waarvan zeker is dat deze niet vaker voorkomen
    # TODO: MODIFY | functie voegt alles toe aan not_lst...
    # TODO: ADD | Schaalbaar?
    pass


def algorithm_complex(antwoord, game_size):
    """
    "Expected Size Strategy"
    testcases
        # antwoord = [4, 2, 3, 3]
        # gok = [3, 5, 3, 5]
        # antwoord = [1, 2, 3, 4]
        # gok = [5, 5, 3, 3]
        # antwoord = [7, 7, 7, 8]
        # gok = [8, 7, 7, 7]
    """
    # TODO: ADD | Een Gevonden ingewikkelde algoritme (mag uit Artikel van Uni Groningen)

    # print(_all_combinations(len(_dict_conversie())))
    g1, g2, g3 = randint(1, len(dict_conversie())), randint(1, len(dict_conversie())), randint(1, len(dict_conversie()))
    for x in range(game_size):
        gok = [g1, g1, g2, g3]

        beoordeling = nakijken(antwoord, gok)

    g4 = randint(1, len(dict_conversie()))
    return [g1, g2, g3, g4]


def algorithm_made(antwoord):
    # TODO: ADD | Zelfgemaakte algoritme
    return None


"""
==========================[Testfunctie]================================
Hieronder testen we de functies.
"""


def initialize_cpu_cpu(antwoord, game_size):
    antwoord_str = [conversie(x) for x in antwoord]
    print(f'\x1b[32m\033[1mCorrecte Combinatie Int: \033[0m\x1b[31m{antwoord}')
    print(f'\x1b[32m\033[1mCorrecte Combinatie Str: \033[0m\x1b[31m{antwoord_str}')

    start = perf_counter()
    print(f'\x1b[32mSimple Teruggegeven: \x1b[31m{algorithm_simple(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mComplex Teruggegeven: \x1b[31m{algorithm_complex(antwoord, game_size)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')

    start = perf_counter()
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{algorithm_made(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


def initialize_user_cpu(antwoord, game_size):
    start = perf_counter()
    antwoord_str = [conversie(x) for x in antwoord]
    print(f'\x1b[32mUser Teruggegeven: \x1b[31m{algorithm_user(antwoord, game_size)}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m in \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


if __name__ == '__main__':
    state = 'W'.lower()  # input(f'\n\n\n\n\x1b[32mPlay or Watch? \x1b[31m(P/W)\x1b[32m: >>> \x1b[31m').lower()

    if state == 'w':
        for c in range(1, 10 + 1):
            print(f'\n\x1b[32m\033[1mSpelnummer: \033[0m\x1b[31m{c}\x1b[32m')
            def_antwoord = reeks()
            initialize_cpu_cpu(def_antwoord, 10)

    elif state == 'p':
        def_antwoord = reeks()
        initialize_user_cpu(def_antwoord, 10)
