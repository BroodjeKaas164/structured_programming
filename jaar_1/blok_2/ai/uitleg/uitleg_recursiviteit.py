def functie(x, y):
    print(f"{x}, {y}")
    if x == 0:
        return y
    return y + functie(x - 1, y)


# x geeft hoeveelheid iteraties mee
# y is resultaat van aantal iteraties van x
print(functie(4, 3))
