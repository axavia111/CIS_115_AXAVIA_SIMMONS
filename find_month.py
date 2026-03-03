#This program allows user to input a value and see if it is in the list

month = input("Enter a month: ") #allows user to input and assigns it to the variable month

def search(month): #define the function and pass the variable month through
    months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December'] #created a list and assigned it to the variables month
    
    if month in months: #if the value entered for the variable month is in the list months than it will print to console
        print(f'The month {month} was found in the list.')
    else:
        print(f'The month {month} was NOT found in the list.')

search(month)
   

