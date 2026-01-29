#This is my program on calculating voltage

current =  input("Enter first number: ") #current is measured in amps
resistance = input("Enter second number: ") #resistance is measured in ohms

voltage = float(current) * float(resistance)
result = voltage

print(f'The voltage is: {result} volts')