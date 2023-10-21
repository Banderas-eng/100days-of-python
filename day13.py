print("""Exam Grade Calculator
---------------------""")
print()
name_of_exam = input("Name of exam: ")
print()
exam_max = int(input("Max. Possible Score: "))
print()
score = float(input("Your score: "))
print()
percentage = (score / exam_max) * 100

#grade is rounded up to 2decimal places
two_decimals = "{:.2f}".format(percentage)

if percentage >= 90:
    print(f"{name_of_exam}: You got {two_decimals}% which is an A+ 😎")
elif percentage >= 80 and percentage < 90:
    print(f"{name_of_exam}: You got {two_decimals}% which is an A- 😊")
elif percentage >= 70 and percentage < 80:
  print(f"{name_of_exam}: You got {two_decimals}% which is a B")
elif percentage >= 60 and percentage < 70:
  print(f"{name_of_exam}: You got {two_decimals}% which is a C")
elif percentage >= 50 and percentage < 60:
  print(f"{name_of_exam}: You got {two_decimals}% which is a D 😥")
else:
  print(f"{name_of_exam}: You got {two_decimals}% which is an F 😢")

