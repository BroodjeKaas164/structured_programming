import datetime
import os


def strftime(filename):
    vandaag = datetime.datetime.today()

    sporters = [[vandaag.strftime("%a %d %b %Y"), '10:45:52', 'Miranda'],
                [vandaag.strftime("%a %d %b %Y"), '10:46:04', 'Piet'],
                [vandaag.strftime("%a %d %b %Y"), '10:47:27', 'Sacha'],
                [vandaag.strftime("%a %d %b %Y"), '10:48:33', 'Karel'],
                [vandaag.strftime("%a %d %b %Y"), '10:48:42', 'Kemal']]

    tijden = open(filename, 'w')
    for sporter in sporters:
        tijden.write(str(sporter) + str('\n'))

    print('\n' + filename, 'created!')


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
    name = 'pe_6_4_hardlopers.txt'
    strftime(name)
    delete(name)


devcode()
