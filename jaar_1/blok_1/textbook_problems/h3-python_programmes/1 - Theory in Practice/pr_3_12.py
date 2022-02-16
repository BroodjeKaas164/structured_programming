import random


def negative(numbers):
    for number in numbers:
        if number < 0:
            print(number)


simplify = [random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000),
            random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000)]
print("Willekeurig gegenereerde lijst: >>>", simplify)

print()
negative(simplify)
