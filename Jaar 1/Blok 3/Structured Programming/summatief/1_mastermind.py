from random import *
# GitHub aanmaken en voeg DavidIsaacspaternostro@hu.nl toe


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


def geheim():  # DONE
    geheim_dict = [choice(range(1, 8)) for x in range(int(4))]
    return geheim_dict


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


def simple_algorithm(antwoord):
    # antwoord = [4, 5, 6, 6]
    gekozen = [x for x in range(len(conversie()) + 1) if x != 0]
    not_list = []  # Voor het opslaan van de waarden die het sws niet zijn.
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
                                        # gekozen.remove(keuze_4)

    # TODO: Modify | Kijk naar beoordeling en haal waarden weg waarvan zeker is dat deze niet vaker voorkomen
    pass


def complex_algorithm(lst):
    # TODO: ADD | Complex Algorithm uit Artikel van Uni Groningen
    pass


def initialize(antwoord):
    # vraag = ['geel', 'wit', 'bruin', 'wit']
    # antwoord = ['groen', 'rood', 'groen', 'wit']
    # print(f'\x1b[31m{vraag}\x1b[32m | \x1b[31m{antwoord}\x1b[32m | \x1b[31m{nakijken(antwoord, vraag)}\x1b[32m')
    print(f'Antwoord: {antwoord}')
    print(f'Teruggegeven: {simple_algorithm(antwoord)}')


if __name__ == '__main__':
    for c in range(20000):
        def_antwoord = geheim()  # ['wit', 'geel', 'geel', 'bruin']
        initialize(def_antwoord)
