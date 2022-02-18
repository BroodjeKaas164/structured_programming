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
        '6': 'Paars'
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


def all_combinations(amount, not_lst):
    """
    Genereert alle mogelijkheden voor het opgegeven aantal.
    :param amount: het aantal verschillende kleuren.
    :param not_lst: lijst met waarden waarvan zeker is dat deze het niet zijn.
    :return: list met alle mogelijkheden
    """
    # TODO: IMPLEMENT | Itertools voor schaalbaarheid?
    amount += 1
    return [[g1, g2, g3, g4] for g1 in range(1, amount) if g1 not in not_lst for g2 in range(1, amount) if g2 not in not_lst for g3 in range(1, amount) if g3 not in not_lst for g4 in range(1, amount) if g4 not in not_lst]


def secret_reeks():  # DONE
    """
    Maakt een willekeurige gegenereerde lijst aan.
    :return: de geheime code
    """
    reeks_dict = [choice(range(1, len(dict_conversie()))) for _ in range(int(4))]
    return reeks_dict


def nakijken(antwoorden_lst, keuze_lst):  # DONE
    """
    Beoordeelt de gegeven combinatie.
    :param antwoorden_lst: de geheime combinatie waarnaar gewerkt moet worden.
    :param keuze_lst: de opgegeven combinatie welke moet voldoen aan de geheime combinatie.
    :return: Dictionary met de beoordeling.
    """
    zwart = wit = 0
    not_index = []
    for x in range(len(antwoorden_lst)):  # Eerst kijken voor 'goed'
        if antwoorden_lst[x] == keuze_lst[x]:
            zwart += 1
            not_index.append(x)

    new_antwoorden_lst, new_keuze_lst = [antwoorden_lst[x] for x in range(len(antwoorden_lst)) if x not in not_index], [keuze_lst[x] for x in range(len(antwoorden_lst)) if x not in not_index]
    for x in range(len(new_antwoorden_lst)):  # Dan kijken voor 'andere plaats' rekening houdend met 'goed'
        if (new_keuze_lst[x] in new_antwoorden_lst) and (wit < antwoorden_lst.count(keuze_lst[x])):  # and (new_keuze_lst.count(new_keuze_lst[x]) < wit)
            wit += 1

    return {'zwart': zwart, 'wit': wit}
