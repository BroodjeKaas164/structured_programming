import random


def allEven(numbers):
    t = 0
    for amount in numbers:
        if (amount % 2) != 0:
            t = t + amount

    if t == 0:
        return True
    else:
        return False


doelEven = [random.randint(1, 2), random.randint(1, 2), random.randint(1, 2)]
print("Random gegenereerde lijst: >>> " + str(doelEven))

print(allEven(doelEven))
