print("Generation Identifier")
print()
year = int(input("Which year are you born? "))
if 1883 <= year <= 1900:
  print("Lost Generarion")
elif 1901 <= year <= 1927:
  print("Greatest Generation")
elif 1928 <= year <= 1945:
  print("Silent Generation")
elif 1946 <= year <= 1964:
  print("Baby Boomer")
elif 1965 <= year <= 1980:
  print("Generation X")
elif 1981 <= year <= 1996:
  print("Millennial")
elif 1997 <= year <= 2012:
  print("Generation Z")
elif 2013 <= year <= 2027:
  print("Generation Alpha")
else:
  print("Generation Beta")  
