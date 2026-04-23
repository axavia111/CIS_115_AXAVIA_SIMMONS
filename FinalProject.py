#Prints a table of the products available
print('-------------------------------------------')
print('            PRODUCT CATALOG                ')
print('-------------------------------------------')
print('1  | USB Drive (128 GB)           |  $12.00')
print('2  | Mac Book Pro (15 in.)        |  $2900.00')
print('3  | Arduino 1010 (w/Bluetooth)   |  $48.00')
print('4  | Ring Camera (wireless)       |  $156.00')
print('5  | Smart TV (TCL 70 in.)        |  $359.00')

#List of dictionaries. Each dictionary containing the info for each product
ListofProducts = [{
    'Product ID': '1',
    'SKU': 'usb_k981',
    'Price': '$12.00',
    'Qty': '',
    'Description': 'USB 128GB drive.',
    'Qty on Hand': '1000'},
    
    {'Product ID': '2',
    'SKU': 'mbpro_490',
    'Price': '$2900.00',
    'Qty': '',
    'Description': 'Mac Book Pro 15 inch.',
    'Qty on Hand': '45'},
   
    { 'Product ID': '3',
    'SKU': 'chip_1010',
    'Price': '$48.00',
    'Qty': '',
    'Description': 'Arduino microprocessor',
    'Qty on Hand': '325'},
    
    {'Product ID': '4',
    'SKU': 'cam_78',
    'Price': '$156.00',
    'Qty': '',
    'Description': 'Ring Camera Model 78.',
    'Qty on Hand': '98'},
    
    {'Product ID': '5',
    'SKU': 'smt_tv_100',
    'Price': '$359.00',
    'Qty': '',
    'Description': 'TCL Smart TV.',
    'Qty on Hand': '225'
    }]


#An empty dictionary for the customer items 
Cart = {}
#Set variable to equal false
validCard = False



def add_to_cart(UserOrder,UserQuantity):
    #sets product to none, to check if the product inputted is found
    product = None 
    #Loops through the catalog to find the corresponding product ID
    for p in ListofProducts: 
        if p['Product ID'] == UserOrder:
            product = p
    #If no product ID was found, let user know invalid ID and exit out of the function
    if product == None:
        print('Invalid Product ID. Please try again.')
        return
    #Converts the string value entered into a integer
    Quantity = int(UserQuantity)
    #Converts the Quantity on hand into a integer
    Qty_on_Hand = int(product['Qty on Hand'])
    #If product is already in the cart, checks what the total quantity would be 
    if UserOrder in Cart:
        #Calculate what to the new Total quantity would be
        QuantityTotal = Cart[UserOrder]['Qty'] + Quantity
       #if the quantity total is more than the quantity available than let user know what is available and what they can get 
        if QuantityTotal > Qty_on_Hand:
          print("Sorry, we only have" + str(Qty_on_Hand) + "of" + product['Description'] +  "available") 
          print("You already have " + str(Cart[UserOrder]['Qty'] + "in your cart"))
          print("You can only add" + str(Qty_on_Hand - Cart[UserOrder]['Qty']) + "to your cart") 
        #Else, it adds on the product in cart instead of making a new entry
        else:
             Cart[UserOrder]['Qty'] += Quantity
   #If quantity entered by user is more than the quantity available and exits out of the function
    else:
        if Quantity > Qty_on_Hand:
             print("Sorry, we only have" + str(Qty_on_Hand) + "of" + product['Description'] + "available")
             return
          
        else:
        #Add a new product with product details
            Cart[UserOrder] = {
                'SKU' : product['SKU'],
                'Price' : product['Price'],
                'Description' : product['Description'],
                'Qty' : Quantity
          }
    

def display_cart():
        #set toal to 0
        total = 0

        #Prints the cart header
        print("----- Your Shopping Cart -----")
        print("Product ID | SKU | Price | Description | Qty")
        print("---------------------------------------------")
        #Loops over the cart and prints each item
        for product, item in Cart.items():
            print(product + " | " + item['SKU'] + " | " + item['Price'] + " | " + item['Description'] + " | " + str(item['Qty']))
            print("------------------------------------------")
            #coverts price to a integer, starting with the first product entered
            price = float(item['Price'][1:])
            #Multiplies price of an item by the quatity then adds to the total amount
            total = total + (price * item['Qty'])
        print("----------------------------------------------")
        #Converts total to a string
        print("Total: $" + str(total))

     
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

 
        

#Prompts user to choose a product from catalog
UserOrder = input("Choose a product ID from the product catalog to continue:  ")
#Prompts user enter how much of the product they would like
UserQuantity = input(f'Enter quantity for product {UserOrder}: ')
#Calls on function
add_to_cart(UserOrder,UserQuantity)

#shows updated cart after user enter product id
display_cart()

#Prompts user again, to see if another product will be added
x = input("Would you like to add another product? (yes or no)?: ")


#If user inputted "yes", than while loop executes, until user inputs "no"
#Calls on funnction to add to the cart each time
#Displays updated cart
while x == "yes":
    UserOrder = input("Choose a product ID from the product catalog to continue:  ")
    UserQuantity = input(f'Enter quantity for product {UserOrder}: ')
    add_to_cart(UserOrder,UserQuantity)
    display_cart()
    x = input("Would you like to add another product? (yes or no)?: ")

#prompt user to see if ready for checkout
checkout = input("Are you ready to checkout? (yes or no): ")
#Keeps asking user until their ready to checkout 
while checkout == "no":
    #Prompts user if they would like to add another product
    anotherItem = input("Would you like to add another item? (yes or no): ")
     #if yes lets user add another product 
    while anotherItem == "yes":
        UserOrder = input("Choose a product ID from the product catalog to continue:  ")
        UserQuantity = input(f'Enter quantity for product {UserOrder}: ')
        add_to_cart(UserOrder,UserQuantity)
        display_cart()
        anotherItem = input("Would you like to add another item? (yes or no): ")
    #Checks to see if user is ready to checkout
    checkout = input("Are you ready to checkout? (yes or no): ")


#if checkout equals yes then prompt for billing/shipping information
if checkout == "yes":
    print("Please enter billing/shipping information")
    print("------------------------------------------")
    first_name = input("Enter Your First Name: ")
    last_name = input("Enter Your Last Name: ")
    address = input("Enter Your Address: ")
    city = input("Enter Your City: ")
    state = input("Enter Your State: ")
    zip_code = input("Enter zipcode/postal code: ")
    email = input("Enter Your Email Address: ")
    phone = input("Enter Your Phone Number: ")

    
    #Prompt for credit card information
while  validCard == False: #While validCard is false than it prompts user for input and reverses the string, and passes it through the function
        ccNum = input("Enter a credit card number: ")   
        ccNum = ccNum[::-1]    
        
        
        if validateCreditCard(ccNum): #Calls on function to check ccNum
                ccNum = ccNum[::-1]
                print(f'The credit card {ccNum} is valid!!!') #The credit card number is valid and validCard is true, so it stops the loop
                validCard = True
                expDate = input("Enter The Expiration Date: ")
                CVV = input("Enter The CVV: ")

        else:
             ccNum = ccNum[::-1]
             print(f'The credit card {ccNum} is invalid. Please try again.') #The credit card number entered is invaild and prompts user to enter another number.
             


    #Displapy billing/shipping information and cart
print("--------------------------------------")
print("---- Billing/Shipping Information ----")
print("---------------------------------------")
print("Name:" + first_name + " " + last_name)
print("Address:" + address)
print("City:" + city)
print("State:" + state)
print("Zip Code:" + zip_code)
print("Email:" + email)
print("Phone:" + phone)

display_cart()











