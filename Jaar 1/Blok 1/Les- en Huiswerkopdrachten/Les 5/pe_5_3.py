def langgenoeg(lengte):
    if lengte >= 120:
        print("Je bent lang genoeg voor de attractie!")
    else:
        print("Sorry, je bent te klein!")


langgenoeg(float(input("Wat is uw lengte?: >>> ")))
