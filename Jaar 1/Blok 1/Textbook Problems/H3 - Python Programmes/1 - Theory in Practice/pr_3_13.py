import random


def f(x, y):
    """average(x, y)
    returns average of x and y"""
    return (x + y) / 2


print(help(f))
a = round(random.uniform(-50, 50), 2)
b = round(random.uniform(-50, 50), 2)
print(a, "-/-", b)
print(f(a, b))

print()


def negative(numbers):
    """negative(numbers)
    prints only negatives within given list"""
    for number in numbers:
        if number < 0:
            print(number)


simplify = [random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000),
            random.randint(-1000, 1000), random.randint(-1000, 1000), random.randint(-1000, 1000)]
print("Willekeurig gegenereerde lijst: >>>", simplify)
negative(simplify)

print(help(negative))
