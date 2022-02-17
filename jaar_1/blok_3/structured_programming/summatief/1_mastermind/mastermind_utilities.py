from random import *


def dict_conversie():  # DONE
    """
    Dictionary met de verschillende kleuren
    :return: Dictionary
    """
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


def conversie(getal):  # DONE
    """
    Converteert de inkomende integer naar de bijbehorende stringwaarde van de Dictionary.
    :param getal: de te converteren waarde.
    :return:
    """
    try:
        return dict_conversie()[str(getal)]
    except KeyError as ke:
        print(ke)


def all_combinations(amount):
    # Itertools?
    amount += 1
    return [[g1, g2, g3, g4] for g1 in range(1, amount) for g2 in range(1, amount) for g3 in range(1, amount) for g4 in range(1, amount)]


def reeks():  # DONE
    """
    Maakt een willekeurige gegenereerde lijst aan.
    :return: de geheime code
    """
    reeks_dict = [choice(range(1, 8)) for x in range(int(4))]
    return reeks_dict


def nakijken(antwoorden_lst, keuze_lst):  # DONE
    zwart = wit = 0
    not_index = []

    for x in range(len(antwoorden_lst)):  # Eerst kijken voor 'goed'
        try:
            if antwoorden_lst[x] == keuze_lst[x]:
                zwart += 1
                not_index.append(x)
        except ValueError as ve:
            print(ve)
        except IndexError as ie:
            print(ie)

    for x in range(len(antwoorden_lst)):  # Dan kijken voor 'andere plaats' zonder rekening te houden voor 'goed'
        try:
            if (keuze_lst[x] in antwoorden_lst) and (antwoorden_lst[x] != keuze_lst[x]) and (keuze_lst[x] not in not_index):  # and (antwoorden_lst.index(antwoorden_lst[x]) not in not_index) and ()
                wit += 1

                b = x
                bruh = antwoorden_lst[x]
                y = antwoorden_lst.index(antwoorden_lst[x])
                pass
        except ValueError as ve:
            print(ve)
        except IndexError as ie:
            print(ie)

    # TODO: MODIFY | In gevallen antw=[x, x, x, y] en kze=[y, x, x, x] geeft {zwart:2, wit:1} --> Moet zijn {zwart:2, wit:2}
    # TODO: MODIFY | In gevallen antw=[a, b, c, d] en kze=[e, e, c, c] geeft {zwart:1, wit:1} --> Moet zijn {zwart:1, wit:0}
    # TODO: MODIFY | In gevallen antw=[c, b, c, d] en kze=[e, e, c, c] geeft {zwart:1, wit:1} --> Moet zijn {zwart:1, wit:1}
    return {'zwart': zwart, 'wit': wit}
