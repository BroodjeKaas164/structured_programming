cijfers = {"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Leo": 2.5, "Martin": 8.0, "Gera": 7.5, "Jan": 9.2}


def hoogvliegers(dict_studenten_cijfers):
    """
    De parameter is een dictionary met studentnamen als sleutels (keys),
    en de cijfers (per student één cijfer) zijn de waarden (values). De
    functie moet een nieuwe dictionary returnen, met daarin de namen (en
    het cijfer) van studenten die een cijfer hoger dan 9,0 hebben.
    Dus {"Gerald": 9.5, "Berend": 4.5, "Bart": 1.0, "Martin": 9.1} levert
    als antwoord: {"Gerald": 9.5, "Martin": 9.1 }]
    Args:
        dict_studenten_cijfers (dict): dictionary met resultaten
    Returns:
        dict: dictionary met resultaten >= 9
    """
    nieuwe_dict = {}
    keys_lijst = dict_studenten_cijfers.keys()
    for student in keys_lijst:
        if dict_studenten_cijfers[student] >= 9:
            nieuwe_dict[student] = dict_studenten_cijfers[student]
    return nieuwe_dict


print(hoogvliegers(cijfers))
