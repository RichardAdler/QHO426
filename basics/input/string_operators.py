lives = int(input("Please enter the number of lives.\n"))
energy = int(input("Please enter the energy level.\n"))
shield = int(input("Please enter the shield level.\n"))
lives_char = "♥" * lives
energy_char = "♦" * energy
shield_char = "♦" * shield
print("\nHealth has been set.")
print("Lives: " + lives_char) 
print("Energy: "+ energy_char)
print("Shield: "+ shield_char)