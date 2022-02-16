def noVowel(s):
    t = ""
    for letter in s:
        if letter in 'aeuioAEUIO':
            t += letter

    if t == "":
        return True
    else:
        return False


print(noVowel(input("Geef woord op: >>> ")))
