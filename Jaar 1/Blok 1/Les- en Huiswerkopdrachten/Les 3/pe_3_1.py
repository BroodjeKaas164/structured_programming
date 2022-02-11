cijferPROJA = 6
cijferPROG = 6
cijferMOD = 6

totaal = (cijferMOD + cijferPROJA + cijferPROG)

gemiddelde = str((totaal / 3))
print('gemiddelde: ' + gemiddelde)
beloning = str((totaal * 30))
print('beloning: ' + beloning)

# 'Mijn cijfers (gemiddeld een 7.5) leveren een beloning van € 675.0 op!'
overzicht = 'Mijn cijfers (gemiddeld een ' + gemiddelde + ') leveren een beloning van €' + beloning + ',- op!'
print(overzicht)
