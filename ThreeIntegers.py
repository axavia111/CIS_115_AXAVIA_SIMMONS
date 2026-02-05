
num1 = int(input('Enter first number: '))

num2 = int(input('Enter second number: '))

num3 = int(input('Enter third number: '))

result = float(num1 + num2) / float(num3)

if(result > 0):
    print("The mathematical operation is > 0")

    print(result)
else:
    print("The mathematical operation is <= 0")

    print(result)