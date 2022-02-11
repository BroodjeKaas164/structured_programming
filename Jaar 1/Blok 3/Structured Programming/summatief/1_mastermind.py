from random import *
# GitHub aanmaken en voeg DavidIsaacspaternostro@hu.nl toe


def conversie_antwoord(getal):
    translatie = {
        '1': 'rood',
        '2': 'oranje',
        '3': 'geel',
        '4': 'groen',
        '5': 'blauw',
        '6': 'wit',
        '7': 'bruin',
        '8': 'zwart',
    }
    return translatie[str(getal)]


def geheim():
    lst_test = [choice(range(1, 8)) for x in range(int(4))]
    geheim_dict = [conversie_antwoord(str(x)) for x in lst_test]
    return geheim_dict


def nakijken(antwoorden_lst, keuze_lst):
    zwart = wit = 0
    not_index = []
    for x in range(len(keuze_lst)):
        if antwoorden_lst[x] == keuze_lst[x]:
            zwart += 1
            not_index.append(keuze_lst[x])
        elif (keuze_lst[x] in antwoorden_lst) and (keuze_lst[x] not in not_index):
            wit += 1

    # TODO Fatal flaw in testcase 2 instanties 'wit' zijn zowel 1 zwart als wit

    beoordeling = {
        'zwart': zwart,
        'wit': wit
    }
    return beoordeling


# TODO: Simple Algorithm uit Artikel van Groningen
def simple_algorithm(lst):
    pass


# TODO: Complex Algorithm uit Artikel van Groningen
def complex_algorithm(lst):
    pass


def initialize(antwoord, vraag):
    vraag = ['geel', 'wit', 'bruin', 'wit']
    antwoord = ['groen', 'rood', 'groen', 'wit']
    print(f'\x1b[31m{vraag}\x1b[32m | \x1b[31m{antwoord}\x1b[32m | \x1b[31m{nakijken(antwoord, vraag)}\x1b[32m')


if __name__ == '__main__':
    def_vraag = geheim()  # ['bruin', 'wit', 'geel', 'bruin']
    def_antwoord = geheim()  # ['wit', 'geel', 'geel', 'bruin']
    for c in range(20):
        initialize(def_antwoord, def_vraag)


