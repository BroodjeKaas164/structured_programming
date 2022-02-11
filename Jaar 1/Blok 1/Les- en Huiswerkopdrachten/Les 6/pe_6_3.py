import os


def analyse(filename):
    maxlijst = []
    infile = open(filename)
    lengteLijst = infile.readlines()
    infile.close()
    for n in range(0, len(lengteLijst)):
        index = lengteLijst[n]
        nummernaam = index.split(', ')
        maxlijst = maxlijst + [nummernaam[0]]
    print('Deze file telt', len(lengteLijst), 'regels.', '\nHet grootste kaartnummer is:', max(maxlijst),
          'en dat staat op regel:', maxlijst.index(max(maxlijst)) + 1)


def writefile(filename):
    infile = open(filename, 'w')
    infile.write('325255, Jan Jansen\n334343, Erik Materus\n235434, Ali Ahson\n645345, Eva Versteeg\n534545, '
                 'Jan de Wilde\n345355, Henk de Vries')


def delete(filename):
    """Optional: File Deletion; will remove clutter in directory"""
    stat = input('Remove File? (Y/N): >>> ')
    if stat == 'Y':
        try:
            os.remove(filename)
            print('\nFile Deleted')
        except:
            print('\nNo File Found')
    else:
        print('File not deleted')


def devcode():
    name = 'pe_6_2_kaartnummers.txt'
    writefile(name)
    analyse(name)
    delete(name)


devcode()
