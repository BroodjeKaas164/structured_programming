def inlezen_beginstation(stations):
    while True:
        begin = input("\nWat is uw beginstation: >>> ")
        if begin in stations:
            print('\tVertreklocatie ingesteld!')
            return begin
        else:
            print('\tDeze trein kan niet uit {} vertrekken'.format(begin))


def inlezen_eindstation(stations, beginstation):
    while True:
        eind = input("\nWat is uw eindstation: >>> ")
        if eind in stations:
            print('\tAankomstbestemming ingesteld!')
            if stations.index(beginstation) < stations.index(eind):
                print('\tTrajectgegevens Ontvangen!')
                return eind
            else:
                if stations.index(beginstation) >= stations.index(eind):
                    print('\tAankomstlocatie kan niet hetzelfde zijn als vertreklocatie!')
                    developement_code()
        else:
            print('\tDeze trein komt niet in {}.'.format(eind))


def omroepen_reis(stations, beginstation, eindstation):
    nummerbegin = stations.index(beginstation) + 1
    nummereind = stations.index(eindstation) + 1

    tegenstations = nummereind - nummerbegin
    kaartprijs = tegenstations * 5

    # '\033[1m' en '\033[0m' opgezocht met 'python bold print console' --> delftstack.com
    a = '\nHet beginstation \033[1m{} is het {}e station\033[0m in het traject.'.format(beginstation, (stations.index(beginstation) + 1))
    b = '\nHet eindstation \033[1m{} is het {}e station\033[0m in het traject'.format(eindstation, (stations.index(eindstation) + 1))
    c = '\nDe afstand bedraagt \033[1m{} station(s)\033[0m.'.format((stations.index(eindstation) - stations.index(beginstation)))
    d = '\nDe prijs van het kaartje is \033[1m{} euro\033[0m.'.format(kaartprijs)
    e = '\n\nJe stapt in de trein in: {}\n\t- '.format(beginstation)
    listf = []
    for n in range(stations.index(beginstation) + 1, stations.index(eindstation)):
        listf.append(stations[n])
    f = '\n\t- '.join(listf)
    g = '\nJe stapt uit in: {}'.format(eindstation)

    return a + b + c + d + e + f + g


def developement_code():
    # Commands/Statements komen uit Canvas: FA 4 NS-Kaartautomaat
    stations = ['Schagen', 'Heerhugowaard', 'Alkmaar', 'Castricum', 'Zaandam', 'Amsterdam Sloterdijk',
                'Amsterdam Centraal', 'Amsterdam Amstel', 'Utrecht Centraal', '’s-Hertogenbosch', 'Eindhoven', 'Weert',
                'Roermond', 'Sittard', 'Maastricht']
    beginstation = inlezen_beginstation(stations)
    eindstation = inlezen_eindstation(stations, beginstation)
    print(omroepen_reis(stations, beginstation, eindstation))

if __name__ == "__main__":
    developement_code()