#This program will use a function to calculate kinetic energy

mass = int(input("Enter your value for mass: "))
velocity = int(input("Enter your value for velocity: "))

def kinetic_energy(mass,velocity):
    KE = .5 * (mass * (velocity ** 2))
    print(f'The objects kinetic energy is: {KE} kgs/mps2')

kinetic_energy(mass,velocity)