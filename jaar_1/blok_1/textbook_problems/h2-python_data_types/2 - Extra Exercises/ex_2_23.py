monthsL = ['Jan', 'Feb', 'Mar', 'May']
monthsT = ('Jan', 'Feb', 'Mar', 'May')

monthsL.insert(3, 'Apr')
# monthsT.insert(3, 'Apr') # // Impossible: Tuples are Immutable

monthsL.append('Jun')
# monthsT.append('Jun') # // Impossible: Tuples are Immutable

monthsL.pop()
# monthsT.pop() * // Impossible: Tuples are Immutable

monthsL.remove('Feb')
# monthsT.remove(1) # // Impossible: Tuples are Immutable

monthsL.reverse()
# monthsT.reverse() # // Impossible: Tuples are Immutable

monthsL.sort()
# monthsT.sort() # // Impossible: Tuples are Immutable
