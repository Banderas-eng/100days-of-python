print("Tip Calculator")
print()
bill = float(input("How much did you spend?: "))
print()
tip = int(input("What percentage do you want to tip?: "))
print()
tipAmount = bill * (tip / 100)
totalBill = bill + tipAmount

numOfPeople = int(input("Enter the number of people: "))
splitBill = totalBill / numOfPeople
splitBill = round(splitBill, 2)
print()
print("You each owe $" + str(splitBill))