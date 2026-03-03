#This program shows how to slice a string value

stringValue = input("Enter a String Value: ") #allows user to input a string value

def slice_my_string(stringValue): #passes whatever the user input assigned to the variable stringValue
    return stringValue[0:3] #returns the position 0 to 3 in value inputed



print (slice_my_string(stringValue)) #calls the function