#This program implements a user-defined function named print_iterations()
Val = int(input("Enter a value: "))
loopCounter = 0


def print_iterations(Val):
    loopCounter = 0

    for i in range(Val):
        loopCounter + 1


    print(f'The function call looped {Val} times.')

print_iterations(Val)