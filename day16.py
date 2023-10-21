count = 1
counter = 1
print("""Fill in the blank spaces!

(Type in the blank space and see if you are cool as me.)""")
print()
while True:
  answer = input("Never going to _____ you up (let, put, give). ")
  print()
  if answer == "let" or answer == "put":
    print("Nope! Try Again.")
    count += 1
    print()
  elif answer == "give":
    break
print("Well done! It took you", count, "attempts")
print()
while True:
  answer1 = input("If I _____ stay (could, want, should). ")
  print()
  if answer1 == "could" or answer1 == "want":
    print("Nope! Try Again")
    counter += 1
    print()
  elif answer1 == "should":
    break
print("Well done! It took you", counter, "attempts")
print()
print("Well done! you took", count + counter, " attempts to complete this exercise")
