#This program calucaltes energy

mass = int(input("Enter a integer value for Mass: "))
c = (int(input("Enter a interger value for C: "))) * 1000000000

def calculate_energy(mass):
    e = mass * (c * c)

    print(f'The energy produced is: {e:,.4f} Joules')

calculate_energy()