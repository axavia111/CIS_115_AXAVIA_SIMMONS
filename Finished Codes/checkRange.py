#This program allows user to enter a integer value to determine if it is in the set range

num1 = int(input("Enter a integer value: "))


while num1 >= 0 and num1 <= 100 :
    num1 = int(input("Enter a integer value: "))

else: 
    print("Sorry, the number you entered is out of range!")
