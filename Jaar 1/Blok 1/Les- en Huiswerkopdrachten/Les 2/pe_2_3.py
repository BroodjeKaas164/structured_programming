# §2.3 Tuples

# De tuple letters kan in willekeurige volgorde de letters A, B en C bevatten. Bijvoorbeeld:
letters = ('A', 'C', 'B', 'B', 'C', 'A', 'C', 'C', 'B')

# Neem deze tuple over, en schrijf code waarmee je een nieuwe lijst maakt met het aantal voorkomens van de letters in
# alfabetische volgorde. Tuple letters bevat 2 keer ‘A’, 3 keer ‘B’ en 4 keer ‘C’. De lijst die dit programma maakt (
# en print) is dan: [2, 3, 4].
lijst = [letters.count('A'), letters.count('B'), letters.count('C')]
print(lijst)
