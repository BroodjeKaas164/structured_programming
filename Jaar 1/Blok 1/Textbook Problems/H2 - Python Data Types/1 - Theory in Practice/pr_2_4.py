# Start by executing the assignment statements:
# >>> s1 = 'ant'
# >>> s2 = 'bat'
# >>> s3 = 'cod'
# Write Python expressions using s1, s2, and s3 and operators + and * that evaluate to:
# (a) 'ant bat cod'
# (b) 'ant ant ant ant ant ant ant ant ant ant '
# (c) 'ant bat bat cod cod cod'
# (d) 'ant bat ant bat ant bat ant bat ant bat ant bat ant bat '
# (e) 'batbatcod batbatcod batbatcod batbatcod batbatcod '

s1 = 'ant'
s2 = 'bat'
s3 = 'cod'

print(s1 + ' ' + s2 + ' ' + s3)
print(10 * (s1 + ' '))
print(s1 + ' ' + (2 * (s2 + ' ')) + (3 * (s3 + ' ')))
print(5 * (s1 + ' ' + s2 + ' '))
print(5 * ((s2 * 2) + s3) + ' ')
