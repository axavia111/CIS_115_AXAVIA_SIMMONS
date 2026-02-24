#This program uses the Pathagorean Theorem to find the hypoteneuse of a right-triangle

def Triangle():

    side_1 = int(input("Enter first number: "))
    side_2 = int(input("Enter second number: "))
    product = (side_1 * side_1) + (side_2 * side_2)
    side_3 = (product) ** .5

    print(f"The missing side is {side_3}")


Triangle()

