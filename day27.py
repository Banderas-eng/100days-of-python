import random
import os, time


def dice(sides):
  result = random.randint(1, sides)
  return result

def health_stats():
  roll_6_sided_roll = dice(6)
  roll_12_sided_roll = dice(12)
  health = ((roll_6_sided_roll * roll_12_sided_roll)/2) + 10
  return health

def strength_stats():
  roll_6_sided_roll = dice(6)
  roll_12_sided_roll = dice(12)
  strength = ((roll_6_sided_roll * roll_12_sided_roll)/2) + 12
  return strength

#print("⚔️ CHARACTER BUILDER ⚔️")
#print()

character = "yes"

while character == "yes":
  os.system("clear")
  print("⚔️ CHARACTER BUILDER ⚔️")
  print()
  legendName = input("Name Your Legend: ")
  print()
  time.sleep(1)
  characterType = input("Character Type (Human, Elf, Wiard, Orc): ")
  print()
  print(legendName)
  
  time.sleep(1)
  print("HEALTH:",str(health_stats()))
  time.sleep(1)
  print("STRENGTH:",str(strength_stats()))
  time.sleep(1)
  print()
  
  print("May your name go down in Legend...")
  print()
  time.sleep(1)
  character = input("Again? (yes/no): ")

  
  
