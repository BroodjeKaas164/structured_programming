# Given the list of student homework grades

grades = [9, 7, 7, 10, 3, 9, 6, 6, 2]

# write:

# (a) An expression that evaluates to the number of 7 grades
print(grades.count(7))

# (b) A statement that changes the last grade to 4
grades[-1] = 4
print(grades)

# (c) An expression that evaluates to the maximum grade
print(grades.count(max(grades)))

# (d) A statement that sorts the list grades
grades.sort()
print(grades)

# (e) An expression that evaluates to the average grade
print(sum(grades) // len(grades))