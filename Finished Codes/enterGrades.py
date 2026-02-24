#This program will allow a user to enter up to 10 grades 

numGrades = int(input("How many grades would you like to enter?  "))
count = 0


while  count < numGrades:
   count = count + 1
   grade = input("Enter your grades: ")

   if(count >= numGrades):
      
      print(f"The user entered {numGrades} grades and is now done.")