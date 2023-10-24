number = 500000
count = 1
while True:
  guess = int(input("Guess a number between 1 and 1000000: "))
  
  if guess < number:
      print()
      print("Too Low")
      print()
  elif number > guess:
      print("Too High")
      print()
  elif guess > 1000000:
    print("Number is above the Margin!")
    print()
  elif guess == number:
    print("Correct!")
    break
  if guess < 1:
    print("Negative numbers NOT accepted!")
    exit()  
  count += 1
  continue

print("It took you", count, "guesses to get it correct!")