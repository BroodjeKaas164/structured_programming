import time
from time import perf_counter
import itertools
from mastermind_utilities import *


def algorithm_user(antwoord, game_size):
    """
    Mastermind waarbij de gebruiker het spel zelf speelt.
    :param antwoord: de geheime combinatie waarnaar gewerkt moet worden.
    :param game_size: de grootte van het spel (het aantal beurten)
    :return:
    """
    antwoord_str = [conversie(x) for x in antwoord]
    tries_int = 0
    tries = []
    tries_str = []
    tries_secret = []

    print('\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n')
    while True:
        print(f'\x1b[32m{dict_conversie()}')
        try:
            # print(f'\x1b[32mAntwoord: >>> \x1b[31m{antwoord}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m')
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
                                        # print(f'\x1b[32mSimple: \x1b[31m{combinations}\x1b[32m')
                                        return [conversie(keuze_1), conversie(keuze_2), conversie(keuze_3), conversie(keuze_4)]
                                    elif (beoordeling['wit'] == beoordeling['zwart'] == 0) and (keuze_4 not in not_list):
                                        not_list.append(keuze_4)


def algorithm_complex(antwoord, game_size):
    """
    testcases
        antwoord = [4, 2, 3, 3]
        gok = [3, 5, 3, 5]
        antwoord = [1, 2, 3, 4]
        gok = [5, 5, 3, 3]
        antwoord = [7, 7, 7, 8]
        gok = [8, 7, 7, 7]
        antwoord = [5, 7, 2, 4]
        gok = [4, 4, 7, 7]
        antwoord = [8, 8, 8, 8]
        gok = [1, 2, 3, 4]
        antwoord = [2, 3, 4, 1]
        gok = [1, 2, 3, 4]

    Het helpt ook niet dat ik het spel eigenlijk nooit heb gespeeld...

    Bron: YouTube Search | "Mastermind Best Strategy"
    Start met Strategie "Per Tweetal"
    Vervolgt met Eigen Strategie
    """
    not_lst = []
    might_lst = []
    getal_1 = getal_2 = 1
    getal_3 = getal_4 = 2
    for poging in range(1, game_size + 1):
        mogelijk = all_combinations(len(dict_conversie()), not_lst)

        # TODO: Modify | Maak de correcte combinatie

        if 1 < poging < len(dict_conversie()) - 1:
            getal_3 += 1
            getal_4 += 1
        if poging > 6:
            getal_3 -= 1
            getal_4 -= 1
        if len(dict_conversie()) - 2 <= poging <= len(dict_conversie()) + 2:
            getal_1 += 1
            getal_2 += 1

        gok = [getal_1, getal_2, getal_3, getal_4]
        beoordeling = nakijken(antwoord, gok)
        # time.sleep(1)
        if beoordeling['zwart'] == 4:
            return gok

        if beoordeling['wit'] == 4:
            might_lst = gok
            not_lst = [x for x in range(len(dict_conversie())) if x not in might_lst]
            print('bruh')

        if beoordeling['wit'] > 0 or beoordeling['zwart'] > 0:
            if getal_1 not in might_lst and getal_1 not in not_lst:
                might_lst.append(getal_1)
            if getal_2 not in might_lst and getal_2 not in not_lst:
                might_lst.append(getal_2)
            if getal_3 not in might_lst and getal_3 not in not_lst:
                might_lst.append(getal_3)
            if getal_4 not in might_lst and getal_4 not in not_lst:
                might_lst.append(getal_4)

        if beoordeling['wit'] == beoordeling['zwart'] == 0:
            if getal_1 not in not_lst:
                not_lst.append(getal_1)
            if getal_2 not in not_lst:
                not_lst.append(getal_2)
            if getal_3 not in not_lst:
                not_lst.append(getal_3)
            if getal_4 not in not_lst:
                not_lst.append(getal_4)
            not_lst.sort()

        try:
            for x in might_lst:
                if x in not_lst:
                    might_lst.remove(x)
        except IndexError as ie:
            pass
        might_lst.sort()

        print(f'\t\x1b[0mMisschien: \x1b[34m{might_lst}\x1b[32m')
        print(f'\t\x1b[0mOnmogelijk: \x1b[34m{not_lst}\x1b[32m')

        print(f'\x1b[32mComplex: \x1b[31m{poging}\x1b[32m | \x1b[31m{[getal_1, getal_2, getal_3, getal_4]}\x1b[32m | \x1b[31m{beoordeling}\x1b[32m')
    return None


def algorithm_made(antwoord):
    # TODO: ADD | Zelfgemaakte algoritme
    return None


"""
==========================[Testfunctie]================================
Hieronder testen we de functies.
"""


def initialize_cpu_cpu(antwoord, game_size):
    # TODO: ADD | TrueTest a.d.h.v. echte use-cases

    antwoord_str = [conversie(x) for x in antwoord]
    print(f'\x1b[32m\033[1mCorrecte Combinatie Int: \033[0m\x1b[31m{antwoord}')
    print(f'\x1b[32m\033[1mCorrecte Combinatie Str: \033[0m\x1b[31m{antwoord_str}\n')

    start = perf_counter()
    print(f'\x1b[32mSimple Teruggegeven: \x1b[31m{algorithm_simple(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms\n')

    start = perf_counter()
    print(f'\x1b[32mComplex Teruggegeven: \x1b[31m{algorithm_complex(antwoord, game_size)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms\n')

    start = perf_counter()
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{algorithm_made(antwoord)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms\n')


def initialize_user_cpu(antwoord, game_size):
    start = perf_counter()
    antwoord_str = [conversie(x) for x in antwoord]
    print(f'\x1b[32mUser Teruggegeven: \x1b[31m{algorithm_user(antwoord, game_size)}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m in \x1b[31m{(perf_counter() - start) * 1000:.0f}ms')


if __name__ == '__main__':
    state = 'w'  # input(f'\n\n\n\n\x1b[32mPlay or Watch? \x1b[31m(P/W)\x1b[32m: >>> \x1b[31m').lower()

    if state == 'w':
        for c in range(1, 1 + 1):
            print(f'\n\x1b[32m\033[1mSpelnummer: \033[0m\x1b[31m{c}\x1b[32m')
            def_antwoord = secret_reeks()
            initialize_cpu_cpu(def_antwoord, 10)

    elif state == 'p':
        def_antwoord = secret_reeks()
        initialize_user_cpu(def_antwoord, 10)
