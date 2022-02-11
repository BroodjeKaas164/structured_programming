import time

t = time.localtime(1500000000)
# Construct the next strings by using the string time format function strftime():
# (a) 'Thursday, July 13 2017'
print(time.strftime('%A, %B %d %Y', t))

# (b) '09:40 PM Central Daylight Time on 07/13/2017'
print(time.strftime('%I:%M%p %Z on %b/%d/%Y', t))

# (c) 'I will meet you on Thu July 13 at 09:40 PM.'
print(time.strftime('I will meet you on %a %B %d at %I:%M%p', t))
