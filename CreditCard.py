#This program checks whether a credit card number is valid or invalid

ccNum = input("Enter credit card number: ") #Prompts user to enter credit card number, needs to be string value in order to loop over each character
x = "Yes"
ccNum = ccNum[::-1] #reverses credit card number

def validateCreditCard(ccNum): #passes the reversed number through
    total = 0 #Keeps track of the sum of numbers passed through loop
    count = 0 #Keeps track of how many times it has been looped over
    
    for number in ccNum:
        num = int(number) #Changes the numbers from string value to integers 

        if count % 2 == 1: #If count retun odd number than it multiplies the numbers by 2
            num = num * 2

            if num > 9: #If number multiplied by 2 is greater than nine, than subtract the product by 9
                num = (num * 2) - 9
    
        total = total + num #Adds the product of the number passed through the loop to the total
        count = count + 1 #Adds the each time it loops over

    return total % 10 == 0 #returns the mod 10 check if the sum of all numbers is equal 0

if validateCreditCard(ccNum): #The credit card number is valid and stops the loop.
    print(f'The credit card {ccNum} is valid!!!')

else:
    print(f'The credit card {ccNum} is invalid. Please try again.') #The credit card number entered is invaild and prompts user to enter another number.
        
        
while x == "Yes":
            x = input("Would you like to enter credit card number?: ") 

            ccNum = input("Enter a credit card number: ") #Keeping the loop going until a valid credit card number is entered
            ccNum = ccNum[::-1]

            validateCreditCard(ccNum) #calls on function to check the next number
    




    