import os


def pretty_print(filename):
    infile = open(filename, 'w')
    infile.write('325255, Jan Jansen\n334343, Erik Materus\n235434, Ali Ahson\n645345, Eva Versteeg\n534545, '
                 'Jan de Wilde\n345355, Henk de Vries')
    infile = open(filename)
    lengteLijst = infile.readlines()
    infile.close()
    for n in range(0, len(lengteLijst)):
        index = lengteLijst[n]
        lijstnummernaam = index.split(', ')
        naam = lijstnummernaam[1].strip('\n')
        print(naam, 'heeft kaartnummer:', lijstnummernaam[0])


def devcode():
    name = 'pe_6_2_kaartnummers.txt'
    pretty_print(name)
    print()
    delete(name)


def delete(filename):
    """Optional: File Deletion; will remove clutter in directory"""
    stat = input('Remove File? (Y/N): >>> ')
    if stat == 'Y':
        try:
            os.remove('pe_6_2_kaartnummers.txt')
        except:
            print('\nNo File Found')
    else:
        print('File not deleted')


devcode()
