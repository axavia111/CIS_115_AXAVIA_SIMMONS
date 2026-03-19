
student_grades = { #a dictionary where each stuent's name is the key and their grade is the value
     'John':  98,
     'Kelly': 95,
     'James': 56,
     'Leland': 78,
     'Chris': 63,
     'Sean': 81}

def calculate_average_grades(student_grades):
    total = 0 #Both total and count are set to 0 before the loop 
    count = 0

    for student, grade in student_grades.items():#allows loop to get both key and value at the same time through each loop
          total = total + grade #keeps a sum of the of all grades as the loop goes
          count = count + 1 #counts how many students were looped through
    average = total / count #Divides the total sum of grades by the number of students were in the loop

    return average #Gives the result out of the function

average = calculate_average_grades(student_grades) #Calls the function

print(f'The average grade is: {average:.2f}') #Print the result with 2 decimal places