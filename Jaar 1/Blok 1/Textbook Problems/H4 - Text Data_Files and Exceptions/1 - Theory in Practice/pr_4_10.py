import os


def myGrep(filename, target):
    infile = open(filename, 'r')
    for line in infile:
        content = line.strip('\n')
        if target in content:
            print(content)


def writefile(filename):
    infile = open(filename, 'w')
    infile.write('The 3 lines in this file end with the new line character.\n\nThere is a blank line above this line.')


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
    name = 'pr_4_10.txt'
    writefile(name)
    myGrep(name, 'line')
    delete(name)


if __name__ == '__main__':
    devcode()
