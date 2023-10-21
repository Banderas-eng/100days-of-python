print("Wholesome Positivity Machine")
print()

name = input("Who are you? ")
print(name)
print()
achieve = input("What do you want to achieve? Teach people to code OR Learn Python! ")
print()

if achieve == "Teach people to code":
  scale = input("On a scale of 1 - 10 how do you feel today? (1: 😢, 10: 😊) ")

  if scale == "1" or scale == "2" or scale == "3" or scale == "4":
    print("Hey", name, "That's not good! Dont worry we are going to help you", achieve, "and you will work with some of our people to up your skills. YOU CAN DO IT 💪!" )
  if scale == "5":
    print("Hey", name, "keep your chin up! Today you're going to help", achieve, "and improve your skills while working with a team - FORGE AHEAD!")
  if scale == "6" or scale == "7":
    print("Hey", name, "keep your chin up! Today you're going to help", achieve, "in the most amazing way, simply being you - YOU ROCK!")
  if scale == "8" or scale == "9" or scale == "10":
    print("Hey", name, "keep your chin up! Today you're going to help", achieve, "in the most amazing way, simply being you - HURAAA!😎")
elif achieve == "Learn Python":
  print("Hey", name, "that's great I guess we can make your dreams come true.")
else:
  print("Sorry we do accept only teachers or tutors. You can Still Work with learn python or work with us a different department!")

########### Another Project ##############

print()
print("""Mean Old Insult Machine
++++++++++++++++++++++""""")
print()
name1 = input("Who are you? ")
if name1 == name1.upper() or name1.lower():
  print(name1)
  print()
  hair = input("How much hair do you have on your head? ")
  if hair == "None" or "none":
    print(hair)
    print()
    scale1 = input("On a scale of 1 - 10 how bald are you? (1: 👱‍♂️, 10: 👨‍🦲) ")
  if scale1 == "8" or scale1 == "9" or scale1 == "10":
    print("Hey", name1, "-yeah thought I wouldn't know who you were because you didn't capitalise properly! Well get that egg-head and dry your eyes beacuse some amazing insults are coming...")
else:
  print("This is NOT a name try again. Please")    