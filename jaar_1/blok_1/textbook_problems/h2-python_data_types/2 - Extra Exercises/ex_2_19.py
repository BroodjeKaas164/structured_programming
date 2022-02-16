answers = ['Y', 'N', 'N', 'Y', 'N', 'Y', 'Y', 'Y', 'N', 'N', 'N']

numYes = answers.count('y')
numNo = answers.count('N')

percentYes = (numYes // len(answers)) * 100
print(percentYes)

answers.sort()
f = answers.index('Y')
print(f)
