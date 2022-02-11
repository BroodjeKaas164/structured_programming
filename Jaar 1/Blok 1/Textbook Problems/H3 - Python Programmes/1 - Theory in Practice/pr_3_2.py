import random

# (a) If age is greater 62, print 'You can get your pension benefits'.
age = float(input("What is your age?: >>> "))

if age >= 62:
    print("you can get your pension benefits!")
else:
    print("Unfortunately, you have to work until 62...")

print("")

# (b) If name is in list ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth'],
# print 'One of the top 5 baseball players, ever!'.
basePlayer = ['Musial', 'Aaraon', 'Williams', 'Gehrig', 'Ruth']
name = input("What's the name of the baseball player?: >>> ")

if name in basePlayer:
    print("One of the top 5 baseball players, ever!")
else:
    print("Is niet Gangster keel...")

print("")

# (c) If hits is greater than 10 and shield is 0, print 'You are dead...'.
defenseFriendly = 100
defenseFoe = 100

speedFriendly = int(random.randint(0, 10))
speedFoe = int(random.randint(0, 10))

print("Speed Friendly: >>> " + str(speedFriendly))
print("Speed Foe: >>> " + str(speedFoe))

print("")

while defenseFoe > 0 or defenseFriendly > 0:
    hitsFriendly = int(random.randrange(5, 15))
    hitsFoe = int(random.randrange(5, 15))

    print("Health Friendly: >> " + str(defenseFriendly))
    print("Health Foe: >> " + str(defenseFoe))

    print("Attack on Foe: >> " + str(hitsFriendly))
    print("Attack on Friendly: >> " + str(hitsFoe))

    if speedFriendly > speedFoe:
        defenseFoe = defenseFoe - hitsFriendly
        if defenseFoe <= 0:
            print("Friendly has won!")
            break
        else:
            defenseFriendly = defenseFriendly - hitsFoe
    else:
        defenseFriendly = defenseFriendly - hitsFoe
        if defenseFriendly <= 0:
            print("Foe has won!")
            break
        else:
            defenseFoe = defenseFoe - hitsFriendly
print("")

# (d) If at least one of the Boolean variables north, south, east, and west is True, print
# 'I can escape.'.
north = bool(random.randint(0, 1))
south = bool(random.randint(0, 1))
east = bool(random.randint(0, 1))
west = bool(random.randint(0, 1))

if north or south or east or west:
    print("I can escape!")
else:
    print("I'm lost...")
