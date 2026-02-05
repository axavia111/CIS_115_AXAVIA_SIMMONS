# This program subtracts two integers and uses if-else logic

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

result = float(num1) - float(num2)

if(result <= 0):
    print('Invalid! The value is less than zero')
    
    print (result)
else:
    print('The values entered were vaild integers.')

    print(result)