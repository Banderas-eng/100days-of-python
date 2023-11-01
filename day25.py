import random

print("⚔ Character Stats Generator ⚔")
print()

def dice(n):
  return random.randint(1,n)
def rolls_dice(n,m):
  health = int()
  health += random.randint(1,6)*random.randint(1,8)
  return health

newCharacter = "yes"
while newCharacter == "yes":
  userCharacter = input("Name your warrior: ")
  print()
  myhealth = rolls_dice(6,8)
  print("Their health is", myhealth,"hp")
  print()
  newCharacter = input("Would you like to create another character?: ")
  print()
