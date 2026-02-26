#This program allows user input to give a start and end month

startMonth = int(input("Enter Start Month: "))
endMonth = int(input("Enter End Month: "))

def months_of_year(startMonth,endMonth):
    months = ['January','Febuary','March','April','May','June','July','August','September','October','November','December']
    return months[startMonth], months[endMonth]




startMonth, endMonth = months_of_year(startMonth,endMonth)

print(f'The Start Month is  {startMonth} and the End Month is {endMonth}')

    
    
    



    
