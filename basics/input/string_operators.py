lives = int(input("Please enter the number of lives.\n"))
energy = int(input("Please enter the energy level.\n"))
shield = int(input("Please enter the shield level.\n"))
lives_char = "♥" * lives
energy_char = "♦" * energy
shield_char = "♦" * shield
print("Health has been set.")
print("Lives: " + str(lives_char)) 
print("Energy: "+ str(energy_char))
print("Shield: "+ str(shield_char))