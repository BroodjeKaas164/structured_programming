import random

# 1
print("Opdracht 1")
leeftijd = int(input("Wat is uw leeftijd?: >>> "))

if leeftijd >= 18:
    print("U mag stemmen!")
else:
    print("Helaas mag u (nog) niet stemmen")

print()

# 2
print("Opdracht 2")
woorden = ['Oplader', 'Laptop', 'Telefoon', 'Sleutels']

for letter in woorden:
    print(letter[0:2])

print()

# 3
print("Opdracht 3")
doelEven = \
    [random.randint(0, 1000), random.randint(0, 1000), random.randint(0, 1000),
     random.randint(0, 1000), random.randint(0, 1000)]
print("Random gegenereerde lijst: >>> " + str(doelEven))

som = 0

for x in doelEven:
    if (x % 2) == 0:
        print("Even: " + str(x))
        som = som + x

print("Opsomming even getallen: >>> " + str(som))
print("")

# 4
print("Opdracht 4")
maandje = int(input("Wat is het nummer van de maand?: >>> "))

if maandje == 3 or maandje == 4 or maandje == 5:
    print("Lente")
elif maandje == 6 or maandje == 7 or maandje == 8:
    print("Zomer")
elif maandje == 9 or maandje == 10 or maandje == 11:
    print("Herfst")
else:
    print("Winter")
