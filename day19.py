print("""Loan Calculator 🧮
-------------------""")
print()
print("\033[33mThis program calculates 5% interest on a loan each year.\033[0m")
print()
amount = float(input("How much did you receive as loan?: "))
print()
for i in range(1, 11):
  amount += (amount * .05)
  print("Year", i, "is", round(amount, 2))
  