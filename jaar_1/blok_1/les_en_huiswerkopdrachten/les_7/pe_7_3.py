studentencijfers = [[95, 92, 86], [66, 75, 54], [89, 72, 100], [34, 0, 0]]


def gemiddelde_per_student(studentencijfers):
    antw = []
    for cijfer in studentencijfers:
        antw.append(sum(cijfer) / len(cijfer))
    return antw


def gemiddelde_van_alle_studenten(studentencijfers):
    """
    antw = []
    for cijfer in studentencijfers:
        antw.append(sum(cijfer) / len(cijfer))
    """
    antw2 = (sum(gemiddelde_per_student(studentencijfers)) / len(gemiddelde_per_student(studentencijfers)))

    return antw2


print(gemiddelde_per_student(studentencijfers))

print(gemiddelde_van_alle_studenten(studentencijfers))
