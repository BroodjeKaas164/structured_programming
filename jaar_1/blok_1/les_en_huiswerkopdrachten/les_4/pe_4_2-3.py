leeftijd = int(input("Wat is uw leeftijd?: >>> "))
pas = input("Nederlands Paspoort? Ja of Nee?: >>> ")

if (pas == 'Ja' or pas == 'ja') and leeftijd >= 18:
    print("U mag stemmen!")
else:
    print("Helaas mag u (nog) niet stemmen")
