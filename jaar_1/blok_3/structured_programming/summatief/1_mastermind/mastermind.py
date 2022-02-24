from time import perf_counter
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
                # TODO: MODIFY | Voeg de keuzes samen in 1 input!
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
                # TODO: MODIFY | index buiten range dictionary van kleuren wordt alsnog toegevoegd aan de lijst met pogingen
                tries_int += 1
                for combination in range(len(tries_str)):
                    print(f'\x1b[31m{combination + 1}\x1b[32m | \x1b[31m{tries[combination]}\x1b[32m | \x1b[31m{tries_str[combination]}\x1b[32m | \x1b[31m{tries_secret[combination]}\x1b[32m')
            if tries_int >= game_size:
                print('\n\x1b[31mHow Unfortunate...\x1b[32m')
                print(f'\x1b[32mAntwoord: \x1b[31m{antwoord}\x1b[32m | \x1b[31m{antwoord_str}\x1b[32m')
                break
        except ValueError as ve:
            print(ve)
    return keuzes


def algorithm_simple(antwoord):
    """
    De Simple Algorithm uit het Artikel van Universiteit Groningen.
    :param antwoord: de geheime combinatie waarnaar gewerkt moet worden.
    :return: tuple met resultaatwaarden die gelijkstaan aan het antwoord
    """
    opties = [x for x in range(len(dict_conversie()) + 1) if x != 0]
    keuze_4 = 1
    not_list = []

    # Zet waarden in not_lst
    gok = [[keuze_1, keuze_2, keuze_3, keuze_4] for keuze_1 in opties if keuze_1 not in not_list for keuze_2 in opties if keuze_2 not in not_list for keuze_3 in opties if keuze_3 not in not_list for keuze_4 in opties if keuze_4 not in not_list]
    beoordeling = [nakijken(antwoord, gok[x]) for x in range(len(gok))]
    for x in beoordeling:
        if x['zwart'] == 4:
            return gok[beoordeling.index(x)]
        if(x['wit'] == x['zwart'] == 0) and (keuze_4 not in not_list):
            not_list.append(keuze_4)


def algorithm_complex(antwoord, game_size):
    """
    Worst Case Strategy?

    Testcases
        Legacy
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

        New
            Gooit alles naar might-lst:
            [1, 3, 5, 2]
            Gooit alles naar might-lst:
            [5, 1, 3, 4]
            Gooit alles naar might-lst:
            [2, 1, 3, 5]

    Het helpt ook niet dat ik het spel nooit heb gespeeld...

    Bron: YouTube Search | "Mastermind Best Strategy".
    Start met Strategie "Per Tweetal" (mix van..)
    Vervolgt met Eigen Strategie.
    """
    not_lst = []

    getal_1 = getal_2 = 1
    getal_3 = getal_4 = 1
    for poging in range(1, game_size + 1):
        mogelijk = all_combinations(len(dict_conversie()), not_lst)

        # TODO: Modify | Maak de correcte combinatie
        # TODO: Modify | Grens van 4 doet moeilijk --> "4 zit in might_lst", terwijl deze "4 in not_lst" moet zijn
        # Oude Statements
        if 1 < poging < len(dict_conversie()):
            getal_3 += 1
            getal_4 += 1
        if poging > 7 and 1 < getal_3 <= len(dict_conversie()) and 1 < getal_4 <= len(dict_conversie()):
            getal_3 -= 1
            getal_4 -= 1
        if len(dict_conversie()) - 2 <= poging <= len(dict_conversie()) + 2:
            getal_1 += 1
            getal_2 += 1

        gok = [getal_1, getal_2, getal_3, getal_4]
        beoordeling = nakijken(antwoord, gok)
        if beoordeling['zwart'] == 4:
            print(f'\x1b[32mComplex: Correct! \x1b[39m{poging}\x1b[32m | \x1b[39m{gok}\x1b[32m | \x1b[39m{beoordeling}\x1b[32m')
            return gok

        if beoordeling['wit'] == 4:
            might_lst = gok
            not_lst = [x for x in range(len(dict_conversie())) if x not in might_lst]

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

        might_lst = [x for x in range(1, len(dict_conversie()) + 1) if x not in not_lst]
        might_lst.sort()

        print(f'\x1b[32mComplex: \x1b[31m{poging}\x1b[32m | \x1b[31m{gok}\x1b[32m | \x1b[31m{beoordeling}\x1b[32m')

        print(f'\t\x1b[0mMisschien: \x1b[33m{might_lst}\x1b[32m')
        print(f'\t\x1b[0mKan Niet: \x1b[37m{not_lst}\x1b[32m')

    pass


def algorithm_made(antwoord, game_size):
    not_lst = []
    might_lst = []

    # antwoord = [1, 3, 4, 2]

    getal_1 = getal_2 = 1
    getal_3 = getal_4 = 1
    for poging in range(1, game_size + 1):
        mogelijk = all_combinations(len(dict_conversie()), not_lst)

        # TODO: Modify | Maak de correcte combinatie
        # TODO: Modify | Grens van 4 doet moeilijk --> "4 zit in might_lst", terwijl deze "4 in not_lst" moet zijn

        """
        # Oude Statements
        if 1 < poging < len(dict_conversie()):
            getal_3 += 1
            getal_4 += 1
        if poging > 7 and 1 < getal_3 <= len(dict_conversie()) and 1 < getal_4 <= len(dict_conversie()):
            getal_3 -= 1
            getal_4 -= 1
        if len(dict_conversie()) - 2 <= poging <= len(dict_conversie()) + 2:
            getal_1 += 1
            getal_2 += 1
        """

        # TODO: MODIFY | Als 1 instantie van getal 3 / getal 4 in antwoord staat --> niks toegevoegd aan not_lst
        if 1 < poging < len(dict_conversie()) + 1:
            getal_1 += 1
            getal_2 += 1

        if (len(dict_conversie()) - 2 <= poging <= len(dict_conversie()) or not not_lst) and (getal_3 < len(dict_conversie()) and getal_4 < len(dict_conversie())):
            getal_3 += 1
            getal_4 += 1

        if not_lst:
            dan_opties = dan_sws_niet = 0
            opties = [x for x in range(len(dict_conversie())) if x not in not_lst and x != 0]
            getal_1 = getal_2 = opties[dan_opties]
            sws_niet = [x for x in range(len(dict_conversie())) if x not in might_lst and x != 0]
            try:
                getal_3 = getal_4 = sws_niet[dan_sws_niet]
            except IndexError as ie:
                pass
            if len(opties) >= dan_opties:
                dan_opties += 1
            if len(sws_niet) >= dan_sws_niet:
                dan_sws_niet += 1

        gok = [getal_1, getal_2, getal_3, getal_4]
        beoordeling = nakijken(antwoord, gok)
        if beoordeling['zwart'] == 4:
            print(f'\x1b[32mSelfmade: Correct! \x1b[39m{poging}\x1b[32m | \x1b[39m{gok}\x1b[32m | \x1b[39m{beoordeling}\x1b[32m')
            return gok

        if beoordeling['wit'] == 4:
            might_lst = gok
            not_lst = [x for x in range(len(dict_conversie())) if x not in might_lst]

        if beoordeling['wit'] == beoordeling['zwart'] == 0:
            if getal_1 not in not_lst:
                not_lst.append(getal_1)
            if getal_2 not in not_lst:
                not_lst.append(getal_2)
            """
            if getal_3 not in not_lst:
                not_lst.append(getal_3)
            if getal_4 not in not_lst:
                not_lst.append(getal_4)
            """

        not_lst.sort()

        might_lst = [x for x in range(1, len(dict_conversie()) + 1) if x not in not_lst]
        might_lst.sort()

        print(f'\x1b[32mSelfmade: \x1b[31m{poging}\x1b[32m | \x1b[31m{gok}\x1b[32m | \x1b[31m{beoordeling}\x1b[32m')

        print(f'\t\x1b[0mMisschien: \x1b[33m{might_lst}\x1b[32m')
        print(f'\t\x1b[0mKan Niet: \x1b[37m{not_lst}\x1b[32m')

    # return lambda x: algorithm_simple(antwoord)  # Wat is lambda? Zoek uit! Bron: Xander <achternaam> - V1A
    print(antwoord)


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
    print(f'\x1b[32mSelfmade Teruggegeven: \x1b[31m{algorithm_made(antwoord, game_size)} \x1b[32min \x1b[31m{(perf_counter() - start) * 1000:.0f}ms\n')


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
            initialize_cpu_cpu(def_antwoord, 12)

    elif state == 'p':
        def_antwoord = secret_reeks()
        initialize_user_cpu(def_antwoord, 10)
