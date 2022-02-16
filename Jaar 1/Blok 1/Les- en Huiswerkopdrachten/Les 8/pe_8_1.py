getallenlijst = []
while True:
    try:
        number = float(input("Geef getal op: >>> "))
        if number == 0:
            break
        else:
            getallenlijst.append(number)
    except:
        print("\tDit is geen geldige invoer.")

print('Er zijn {} getallen ingevoerd, de som is: {}'.format(len(getallenlijst), sum(getallenlijst)))
