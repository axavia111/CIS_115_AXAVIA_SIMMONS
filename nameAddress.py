#This program returns the key and values of the dictionary names and addresses
names_and_addresses = [{  #a list that holds mutiple dictionaries for each person
     'firstName':  'Carl',
     'lastName': 'Dove',
     'city': 'Sanford',
     'state': 'Lousianna',
     'zipCode': '287788',
     'phoneNumber': '555-2337'},
    { 
     'firstName':  'Lynn',
     'lastName': 'Oswald',
     'city': 'Raleigh',
     'state': 'North Carolina',
     'zipCode': '389955',
     'phoneNumber': '555-2664'},
     { 
     'firstName':  'Sean',
     'lastName': 'Dean',
     'city': 'Fayetteville',
     'state': 'Georgia',
     'zipCode': '387955',
     'phoneNumber': '555-2569'}]

def print_dictionary(names_and_addresses): #a function that accepts the list as a full argument
    print(names_and_addresses) #prints each dictionary

print_dictionary(names_and_addresses) #calls the function and prints it out
