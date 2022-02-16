import random

# Opdracht 4.4
week = ['maandag', 'dinsdag', 'woensdag']

for dag in week:
    print(dag[0:2])

print("")

# Opdracht 4.5
doelEven = \
    [random.randint(0, 10000), random.randint(0, 10000), random.randint(0, 10000),
     random.randint(0, 10000), random.randint(0, 10000)]
print("Random gegenereerde lijst: >>> " + str(doelEven))

for x in doelEven:
    if (x % 2) == 0:
        print("Even: " + str(x))

print("")

# Opdracht 4.6
s = "Maarten van Rossum heeft programmeertaal Python bedacht."
t = ""
for letter in s:
    if letter in 'aeoiuAEIOU':
        t += letter
print(t)
