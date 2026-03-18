#This program shows how to slice a list

months = ['January','Feburary','March','April','May','June','July','August','September','October','November','December'] #This list uses months of the year and assigns it to month variable

def slice_list(months):#This function passes the month variable through
    return months[4:7] #Since I want the months in position 4 - 6;with 6 inclusive. I used position 7 as the end position


print(slice_list(months)) #Prints/calls the function

