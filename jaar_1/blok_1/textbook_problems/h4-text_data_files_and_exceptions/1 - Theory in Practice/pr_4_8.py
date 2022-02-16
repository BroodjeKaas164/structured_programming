import os


def stringCount(filename, target):
    """returns the number of characters in file filename"""

    infile = open(filename, 'w')
    infile.write('The 3 lines in this file end with the new line character.\n\nThere is a blank line above this line.')
    infile = open(filename, 'rt')
    content = infile.read()
    occurrence = content.count(target)
    infile.close()

    return occurrence


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
    name = 'pr_4_8_example.txt'
    print(stringCount(name, 'line'))
    print()
    delete(name)


if __name__ == '__main__':
    devcode()
