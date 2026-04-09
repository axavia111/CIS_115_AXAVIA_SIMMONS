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
    #If product is already in the cart, the cart updates with added quantity value, instead of adding new entry
    if UserOrder in Cart:
        Cart[UserOrder]['Qty'] += Quantity
    else:
        pass
        



#Prompts user to choose a product from catalog
UserOrder = input("Choose a product ID from the product catalog to continue:  ")
#Prompts user enter how much of the product they would like
UserQuantity = input(f'Enter quantity for product {UserOrder}: ')
#Calls on function
add_to_cart(UserOrder,UserQuantity)


#Prompts user again, to see if another product will be added
x = input("Would you like to add another product (yes or no)?: ")


#If user inputted "yes", than while loop executes, until user inputs "no"
while x == "yes":
    UserOrder = input("Choose a product ID from the product catalog to continue:  ")
    UserQuantity = input(f'Enter quantity for product {UserOrder}: ')
    add_to_cart(UserOrder,UserQuantity)
    x = input("Would you like to add another product (yes or no)?: ")










