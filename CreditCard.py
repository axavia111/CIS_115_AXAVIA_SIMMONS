#This program checks whether a credit card number is valid or invalid

ccNum = (input("Enter credit card number: ")) #Prompts user to enter credit card number, needs to be string value in oder to loop over each character

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
    
    total = total + num
    count = count + 1

    return total % 10 == 0 #returns the mod 10 check if equals to 0

if validateCreditCard(ccNum):
    print(f'The credit card entered is valid!!!!')