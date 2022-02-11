import json

# Copyright | Gerard Ovink 2021

with open('/Jaar 1/Blok 1/Les- en Huiswerkopdrachten/Les 10/sporen.json', 'r') as json_file:
    data = json.load(json_file)
    stations = data["payload"]
    print(stations)
    meest_oost = (-181.0, '')

    print('Dit zijn de namen, codes en types van elk station:')
    for station in stations:
        code = station['code']
        type = station['stationType']
        naam = station['namen']['lang']
        long = station['lng']

        if float(long) > meest_oost[0]:
            meest_oost = (long, naam)

        print('{:24} - {:5} : {}'.format(naam, code, type))

    print('\nHet meest oostelijk gelegen station is: {}'.format(meest_oost[1]))
