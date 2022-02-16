# §3.3 Input / Output (Formatief)

# Hier wordt de gebruiker gevraagd voor 'uurloon' en 'uurgewerkt' om later te kunnen gebruiken voor de berekening
# naar 'salaris'.
uurloon = float(input('Wat is uw uurloon? >> '))
uurgewerkt = float(input('Hoeveel uur heb je gewerkt? >> '))

# Hier wordt het salaris berekend in float (komma-getallen) --> dan wordt er afgerond op 2 decimalen -->  daarna
# wordt het resultaat omgezet in STRING, zodat compatibiliteit met de laatste regel mogelijk wordt gemaakt
salaris = round((uurloon * uurgewerkt), 2)

# Hier wordt het resultaat gepresenteerd in en makkelijk overzicht.
print(str(uurgewerkt) + ' uur werken levert €' + str(salaris) + ' op.')
