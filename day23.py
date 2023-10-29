from getpass import getpass as input

print("|| Replit Login System ||")
print()

def login():
  while True:
    username = input("What is your Username?: ")
    print()
    password = input("What is your password?: ")
    print()
    if username == "david" and password == "baldies4life":
      print("\033[0;32mWelcome to REPLIT!")
      break
    else:
      print("\033[33mWhoops! I don't recognize that username or password. Try Again!\033[0m")
      print()
    continue

login()