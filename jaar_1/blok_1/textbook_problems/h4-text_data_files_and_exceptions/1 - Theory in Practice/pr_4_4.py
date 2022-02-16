# Write function even() that takes a positive integer n as input and prints on the screen all numbers between,
# and including, 2 and n divisible by 2 or by 3, using this output format:
def even(n):
    for x in range(2, n + 1):
        if x % 2 or x % 3:
            print(x, end=', ')


even(int(input("Insert number: >>> ")))
