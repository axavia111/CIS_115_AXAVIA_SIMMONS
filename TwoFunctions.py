#This program implements two functions

def print_message1():
    print('I was called first.')
    
    print_message2()
    return

def print_message2():
    print("I was called from print_message1()")
     
    return


print_message1()