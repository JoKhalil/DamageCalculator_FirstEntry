# Highest Defense is 230 average is 152 and lowest is 75
import math

FIRST = int(2)
SECOND = int(5)
THIRD = int(2)
FOURTH = int(50)
FIFTH = int(2)

level = int(input("Enter your pokemon's level : "))
power = int(input("Enter the move's power points : "))
attack = int(input("Enter your pokemon's attack stats : "))
defense = int(input("Enter the enemy's defense stats : "))
targets = float(input("Enter the number of target (0.75 if more than 1 else 1): "))
weather = float(input("Enter the weather stats (1.50 if weather helps 0.50 if weather cuts): "))
badge = int(input("Enter the badge stat (Gen 2 ONLY) : "))
critical = float(input("Enter the crit multiplier (Gen 3-5 is x2 Gen 6-8 is x1.5) : "))
random = 0.85
stab = float(input("Enter the STAB multiplier (1.5 if same type and 2 if pokemon has Adaptability) : "))
type = float(input("Enter the type multiplier (0.25, 0.50, 1 , 2 or 4) : "))
burn = float(input("Enter the burn multiplier (0.50 if ability is not Guts and move is physical) : "))
other = int(input("Enter the other multiplier (item multiplier) : "))

damage = ((((math.floor(FIRST * level / SECOND) + THIRD) * power * attack / defense / FOURTH) + FIFTH)) * math.floor(targets * weather) * math.floor(badge * stab) * math.floor(type * burn) * other

print("The move will do between " + str(damage * random) +" and " + str(damage) + " raw damage to the enemy \n and it could do between " + str(damage * random * critical) + " and " + str(damage * critical))