#This program calucaltes energy

mass = float(input("Enter a integer value for Mass: "))
c = 2.99 * 10**8


def calculate_energy(mass):
    e = mass * (c * c)

    print(f'The energy produced is: {e:,.6f} Joules')

calculate_energy(mass)