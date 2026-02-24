#This program will use lists and for-loop over the list and print it out

def getMylist():
    list = [10,20,30,40,50,60]

    length = len(list)
    
    for item in list:
        
        print(item)

    return length
total = getMylist()
print(f'The total count is : {total}')
