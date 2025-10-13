#Take a temperature value and print "cold", "warm", or "hot" using range conditions
temper=int(input("Enter the temperature : "))
if temper>30:
    print(" Hot")
elif (temper>=20 and temper<=30):
    print("Warm")
else:
    print("Cold")