#This program allows user to append to a list


list = [1,2,3,4,5,6] #The list is already defined

def append_to_list(value,list): #This function passes the list and the value entered; Then the value is then added to the list at the end
    list.append(value)   
    return list

value = input("Enter a value: ") #Prompt user to enter any value
append_to_list(value,list)


x = input("Would you like to enter another value to append to the list?:  ") #Prompts user again to enter a value

while x  == 'yes': #Uses a while-loop and keeps prompting user to enter a value to add to the list. 
    value = input("Enter a value: ")
    append_to_list(value,list)
    x = input("Would you like to enter another value to append to the list?:  ") #Once x == no, then the loop stops.

print(list) #Prints out the list with the values user inputted

