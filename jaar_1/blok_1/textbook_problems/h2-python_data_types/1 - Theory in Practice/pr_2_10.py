import math

# Write Python expressions corresponding to the following:

# (a) The length of the hypotenuse in a right triangle whose other two sides have lengths a and b
(ab, bc) = (3, 4)
ac = math.sqrt((ab**2) + (bc**2))
# ac = sqrt(25) = 5

# (b) The value of the expression that evaluates whether the length of the above hypotenuse is 5
print(int((ab**2) + (bc**2) == (ac**2)))


# (c) The area of a disk of radius a
print(math.pi * (ab**2))

# (d) The value of the Boolean expression that checks whether a point with coordinates x and y
# is inside a circle with center (a, b) and radius r
(x, y) = (2, 4)
(a, b) = (-3, 5)
print(((x - a)**2) + ((y - b)**2) < (6**2))
