def aantal_kluizen_vrij():
    """DONE: Retourneert het aantal beschikbare kluizen"""

    file = open(__my_test_file(), 'r')
    return 12 - len(file.readlines())


def nieuwe_kluis():
    """DONE: User maakt unieke code voor zijn/haar kluis en retourneert gebruikte kluisnummer"""

    file = open(__my_test_file())
    if len(file.readlines()) <= 12:
        print('\tEr zijn {} kluizen beschikbaar.'.format(aantal_kluizen_vrij()))
    else:
        print('\tHelaas is er geen kluis meer beschikbaar')
        return -2

    file = open(__my_test_file())
    content = file.readlines()
    kluisnummers = []
    for n in range(0, len(content)):
        index = content[n]  # Leest bestand in naar lijst
        noPK = index.split(';')  # Split kluisnummer en Kluiscode
        code = noPK[1].strip('\n')  # Haalt 'nextLine' weg
        noPK[1] = code  # Isoleert Kluiscode
        kluisnummers.append(int(noPK[0]))  # Voegt Kluisnummer toe aan lijst
    kluisnummers.sort()
    print('\tKluizen in gebruik: {}'.format(kluisnummers))

    while True:
        kluis = int(input('\nWelke kluisnummer: >>> '))
        if (0 < kluis <= 12) and (kluis not in kluisnummers):
            print('\tGeaccepteerd: kluis gekozen!')
            break
        else:
            print('\tGeweigerd: Geen geldig kluisnummer!')

    while True:
        code = input('\nGeef een unieke wachtwoord.\nLET OP: deze moet langer zijn dan 4 tekens en mag geen {} '
                     'bevatten: >>> '.format(';'))
        if (len(code) >= 4) and (code.find(';') == -1):
            print('\tGeaccepteerd: Code van kluis is ingesteld!')
            break
        else:
            print('\tGeweigerd: Geen geldige code!')
            if len(code) < 4:
                print('\t\tReden: De code is korter dan 4 tekens.')
            elif code.find(';') != -1:
                print('\t\tReden: De code bevat {}.'.format(';'))

    if True:
        file = open(__my_test_file(), 'a')

        file.write(str(kluis))
        file.write(';')
        file.write(str(code))
        file.write('\n')

    return kluis


def kluis_openen():
    """DONE: open de kluis tijdelijk voor gebruik"""

    file = open(__my_test_file())
    content = file.readlines()
    kluisnummers = []
    kluiscodes = []
    for n in range(0, len(content)):
        index = content[n]  # Leest bestand in naar lijst
        noPK = index.split(';')  # Split kluisnummer en Kluiscode
        code = noPK[1].strip('\n')  # Haalt 'nextLine' weg
        noPK[1] = code  # Isoleert Kluiscode
        kluisnummers.append(int(noPK[0]))  # Voegt Kluisnummer toe aan lijst
        kluiscodes.append(noPK[1])
    print('\tKluizen in gebruik: {}'.format(kluisnummers))

    while True:
        kluis = int(input('\nGeef uw kluisnummer op: >>> '))
        if kluis in kluisnummers:
            print('\tGeaccepteerd: Geldige invoer')
            break
        else:
            print('Geweigerd: Geen geldige invoer.')

    # print(kluiscodes[kluisnummers.index(int(kluis))])         # Wachtwoordstatement voor overzicht
    while True:
        if input('\nGeef uw wachtwoord van de kluis op: >>> ') == kluiscodes[kluisnummers.index(int(kluis))]:
            print('\tGeaccepteerd: Kluiscode is correct.\n\tKluis {} is geopend!'.format(kluis))
            return True
        else:
            print('\tGeweigerd: Kluiscode is incorrect.')


def kluis_teruggeven():
    """OPTIONEEL | DONE: Verwijdert ingevoerde kluis op verzoek van user."""
    file = open(__my_test_file())
    content = file.readlines()
    kluisnummers = []
    kluiscodes = []
    for n in range(0, len(content)):
        index = content[n]  # Leest bestand in naar lijst
        no_pk = index.split(';')  # Split kluisnummer en Kluiscode
        code = no_pk[1].strip('\n')  # Haalt 'nextLine' weg
        no_pk[1] = code  # Isoleert Kluiscode
        kluisnummers.append(int(no_pk[0]))  # Voegt Kluisnummer toe aan lijst
        kluiscodes.append(no_pk[1])
    print('\tKluizen in gebruik: {}'.format(kluisnummers))

    while True:
        kluis = int(input('\nWelke kluisnummer: >>> '))
        if (0 < kluis <= 12) and (kluis in kluisnummers):
            print('\tGeaccepteerd: kluis gekozen!')
            break
        else:
            print('\tGeweigerd: Geen geldig kluisnummer!')

    # print(kluiscodes[kluisnummers.index(int(kluis))])         #  Wachtwoordstatement voor overzicht
    while True:
        if input('\nGeef uw wachtwoord van de kluis op: >>> ') == kluiscodes[kluisnummers.index(int(kluis))]:
            file = open(__my_test_file(), "r")
            contents = file.readlines()
            file.close()
            contents.pop(kluisnummers.index(int(kluis)))

            file = open(__my_test_file(), "w")
            contents = "".join(contents)        # '.join'-command van Stackoverflow -@ungalcrys
            file.write(contents)
            file.close()

            print('\tGeaccepteerd: Kluiscode is correct.\n\tKluis {} is verwijderd!'.format(kluis))
            return True
        else:
            print('\tGeweigerd: Kluiscode is incorrect.')




def development_code():
    """DONE: FA 3 - Bagagekluizen ; Keuzemenu binnen de applicatie"""
    
    try:
        writefile(__my_test_file())
        file = open(__my_test_file())
    except:
        file = open(__my_test_file(), 'w')

    while True:
        print('\nKies een optie:')
        print("1: Aantal kluizen vrij")
        print("2: Nieuwe kluis aanvragen")
        print("3: Kluis uithalen")
        print("4: Kluis inleveren")
        print("\n5: Programma Afsluiten")
        choice = input("\nGeef keuze op: >>> ")

        try:
            if int(choice) == 1:
                print('Aantal kluizen vrij: {}'.format(aantal_kluizen_vrij()))
            elif int(choice) == 2:
                print('\nAangewezen kluis: {}'.format(nieuwe_kluis()))
            elif int(choice) == 3:
                kluis_openen()
                print('\nKluis is geopend.')
            elif int(choice) == 4:
                kluis_teruggeven()
                print('\nKluis is verwijderd.')
            elif int(choice) == 5:
                break
            else:
                print('\tDit is geen geldige keuze.')

        except ValueError:
            print("\tSysteemfout: Invoer geen getal!")

    file.close()
    print('Tot ziens en een fijne dag!')


def __my_test_file():
    """DONE: Retourneert een naam voor het (aan te maken)/(wijzigen) van het bestand"""
    return "fa_3_kluizen.txt"


def writefile(filename):
    open(filename)


development_code()
