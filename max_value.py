#This program returns the max value of two integer values entered

num1 = int(input('Enter first value: '))
num2 = int(input('Enter second value: '))

def max(num1,num2):
    if num1 < num2:
     print(num2)
    else:
       print(num1)
    
max(num1,num2)