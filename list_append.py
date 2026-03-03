
value = input("Enter a value: ")
list = [1,2,3,4,5,6]
def append_to_list(value):
    
    list.append(value)
    return list

x = input("Would you like to enter another value to append to the list?: ")

while x  == 'y':
    value = input("Enter a value: ")
    x = input("Would you like to enter another value to append to the list?: ")
    append_to_list(value)


print(list)

