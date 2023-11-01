from replit import audio
import os, time

def play():
  source = audio.play_file('audio.wav')
  source.paused = False # unpause the playback
  while True:
    # Start taking user input and doing something with it
    print()
    exit = input("Press 2 to Exit: ")
    if exit == "2":
      source.paused = True
      print()
      print("Exiting...")
      time.sleep(1)
      break
    else:
      continue
    #exit = input("Press 2 to Exit: ")
      

while True:
  # clear the screen 
  os.system('clear')
  print("🎶 MyPOD Music Player")
  print()
  
  # Show the menu
  print("Menu 📜")
  print()
  print("Press 1 to Play")
  time.sleep(1)
  print()
  print("Press 2 to Exit")
  time.sleep(1)
  print()
  print("Press anything else to see the new menu again")
  time.sleep(1)

  # take user's input
  choice = input()

  # check whether you should call the play() subroutine depending on user's input
  if choice == "1":
    print()
    print("Playing some proper tunes!")
    play()
  elif choice == "2":
    exit()
  else:
    continue
