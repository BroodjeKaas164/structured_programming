"""
print('i i**2 i**3 2**i')
for i in range(1, 13):
    print(i, i**2, i**3, 2**i, sep='\t\t')

# print('{:8.4}'.format(1000 / 3))

n = 10

print('{:b}'.format(n))
print('{:c}'.format(n))
print('{:d}'.format(n))
print('{:o}'.format(n))
print('{:x}'.format(n))
print('{:X}'.format(n))
"""


def roster(gradelist):
    print('{:10} {:10} {:10} {:8}'.format('Last', 'First', 'Class', 'Average Grade'))
    for stud in gradelist:
        print('{:10} {:10} {:10} {:8.2}'.format(stud[0], stud[1], stud[2], stud[3]))


students = [['DeMoines', 'Jim', 'Sophomore', 3.45], ['Pierre', 'Sophie', 'Sophomore', 4.0],
            ['Columbus', 'Maria', 'Senior', 2.5], ['Phoenix', 'River', 'Junior', 2.45],
            ['Olympis', 'Edgar', 'Junior', 3.99]]
roster(students)
