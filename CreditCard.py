#This program checks whether a credit card number is valid or invalid


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

    return total % 10 == 0 #returns the mod 10 check if the product is equal 0

validCard = False #Set variable to equal false 
        
while  validCard == False: #While validCard is false than it prompts user for input and reverses the string, and passes it through the function
    ccNum = input("Enter a credit card number: ")   
    ccNum = ccNum[::-1]    
        
        
    if validateCreditCard(ccNum): #Calls on function to check ccNum
                ccNum = ccNum[::-1]
                print(f'The credit card {ccNum} is valid!!!') #The credit card number is valid and validCard is true, so it stops the loop
                validCard = True

    else:
             ccNum = ccNum[::-1]
             print(f'The credit card {ccNum} is invalid. Please try again.') #The credit card number entered is invaild and prompts user to enter another number.
             




    
        




    