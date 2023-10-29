print("Math Multplication TimeTable Game! ✖")
print()
timetable = int(input("Name your multiples: "))
score = 0
for i in range(1, 13):
  print(i, "x", timetable)
  multiple = i * timetable
  answer = int(input("= "))
  if answer == multiple:
    print("Great Work! 🥳")
    score += 1
  else:
    print("Nope! 😒 The answer is", multiple)
if score == 12:
  print("Congratulations!🥳 You got all CORRECT!🎉 ")
else:
  print("You have", score, "out of 12. CAN DO BETTER 👍")  
    