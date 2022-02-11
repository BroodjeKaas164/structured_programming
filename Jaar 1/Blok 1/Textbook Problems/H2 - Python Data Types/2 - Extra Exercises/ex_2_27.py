import math

length = float(input('Length of Ladder: >> '))
angle = float(input('Angle of Ladder: >> '))

height = round(length * math.sin(((math.pi * angle) / 180)), 2)

print('The height reached with ' + str(length) + ' feet and ' + str(angle) + ' degrees, is ' + str(height) + ' feet!')
