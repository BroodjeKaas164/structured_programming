import os


def words(filename):
    """Converts a file to a string"""

    infile = open(filename, 'r')
    content = infile.read()
    infile.close()

    table = str.maketrans('!,.:;?', 6 * ' ')
    content = content.translate(table)
    content = content.lower()
    return content.split()


def writefile(filename):
    infile = open(filename, 'w')
    infile.write('The 3 lines in this file end with the new line character.\n\nThere is a blank line above this line.')


def delete(filename):
    """Optional: File Deletion; will remove clutter in directory"""
    stat = input('Remove File? (Y/N): >>> ')
    if stat.upper() == 'Y':
        try:
            os.remove(filename)
            print('\nFile Deleted')
        except:
            print('\nNo File Found')
    else:
        print('File not deleted')


def devcode():
    name = 'pr_4_9.txt'
    writefile(name)
    print(words(name))
    delete(name)


if __name__ == '__main__':
    devcode()
