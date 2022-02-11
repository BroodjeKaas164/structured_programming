import random

# (a) If year is divisible by 4, print 'Could be a leap year.'; otherwise print 'Definitely not
# a leap year.'
year = int(input("What year is it?: >>> "))

if (year % 4) == 0:
    print("This is a Leap Year!")
else:
    print("This ain't it chief")

# (b) If list ticket is equal to list lottery, print 'You won!'; else print 'Better luck next
# time...'

ticket = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]
lottery = [random.randint(0, 1), random.randint(0, 1), random.randint(0, 1)]

print("Ticket: " + str(ticket))
print("Ticket: " + str(lottery))

if ticket == lottery:
    print("You win")
else:
    print("Ripperoni in Pepperoni")
