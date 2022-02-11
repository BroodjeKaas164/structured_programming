import os


def gemiddelde(lijst):
    totaal = 0
    for woord in lijst:
        totaal = totaal + len(woord)

    print('{:.3}'.format(float(totaal / len(lijst))))


def listcreate(filename, zin):
    infile = open(filename, 'w')
    infile.write(zin)

    infile = open(filename, 'r')
    content = infile.read()
    woordenlijst = content.split()
    return woordenlijst


def delete(filename):
    """Optional: File Deletion; will remove clutter in directory"""
    stat = input('\nRemove File? (Y/N): >>> ')
    if stat.upper() == 'Y':
        try:
            os.remove(filename)
            print('\nFile Deleted')
        except:
            print('\nNo File Found')
    else:
        print('\nFile not deleted')


def devcode():
    zin = input('Gooi ff zin toe: >>> ')
    name = 'userEntry.txt'
    gemiddelde(listcreate(name, zin))
    delete(name)


if __name__ == '__main__':
    devcode()
