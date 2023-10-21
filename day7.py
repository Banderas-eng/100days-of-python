print("""🕵️‍♀️ Fake Fan Finder 👀
----------------------""")
print()

anime = input("What is your favorite Anime?: ")
if anime == "One Piece":
    character = input("Oh really! Name any of the characters?: ")
  
    if character == "Nami":
        job = input("You got that by pure chance. Okay then, what is her job on the ship?: ")
    if job == "Navigator":
      bounty = input("Hmph! What was her first bounty then?: ")
    else:
      print("You are not a fan of anime.")
    if bounty == "Ummm!":
        print("See! FAKE one piece fan!")
    else:
      print("Hmmm will get back to you")      
else:
  print("You are not a one piece fan!")