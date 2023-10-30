import random

print("Infinity Dice 🎲")
print()

exit = "yes"
sides = int(input("How many sides?: "))
print()
def rollDice(sides):
  print()
  print("You rolled", random.randint(1, sides))
  print()
while exit == "yes":
  print()
  print("Rolling Dice...")
  print()
  rollDice(sides)
  print()
  exit = input("Roll again?: ")
      

          
