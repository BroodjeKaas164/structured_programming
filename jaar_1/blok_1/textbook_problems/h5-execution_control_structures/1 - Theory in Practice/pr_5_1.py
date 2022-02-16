def myBMI(height, weight):
    return (weight * 703) / (height ** 2)


height = (float(input("Height in Inches: >>> ")))
weight = (float(input("Weight in Pounds: >>> ")))

if myBMI(height, weight) < 18.5:
    print("Underweight")
elif 8.5 <= myBMI(height, weight) < 25:
    print('Normal')
elif myBMI(height, weight) >= 25:
    print('Overweight')