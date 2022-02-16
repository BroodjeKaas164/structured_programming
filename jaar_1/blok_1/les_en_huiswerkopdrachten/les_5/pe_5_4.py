# Schrijf (en test) een functie new_password() die 2 parameters heeft: oldpassword en newpassword. De return-waarde
# is True als het nieuwe password voldoet aan de eisen. Het nieuwe password wordt alleen geaccepteerd als het
# verschilt van het oude password èn als het minimaal 6 tekens lang is. Als dat niet zo is, is de return-waarde False.
# Optioneel: zorg dat het nieuwe password minstens 1 cijfer moet bevatten!

def new_password(oldpassword, newpassword):
    if (len(newpassword) >= 6) and (oldpassword != newpassword) and any(map(str.isdigit, newpassword)):
        return True
    return False


print("Change Password:")
print()
old = input("Old password: >>> ")
new = input("New password: >>> ")

print(new_password(old, new))
