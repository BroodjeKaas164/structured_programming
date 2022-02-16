

def arithmetic(lijstje):
    if len(lijstje) < 2:
        return True
    verschil = lijstje[1] - lijstje[0]
    for i in range(1, len(lijstje) - 1):
        if lijstje[i + 1] - lijstje[i] != verschil:
            return False
    return True


print(arithmetic([3, 6, 9, 12, 15]))
print(arithmetic([3, 6, 9, 11, 14]))
print(arithmetic([3]))
