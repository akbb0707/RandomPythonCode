# Authentication
enteredPlayerName = input("Enter your name: ")
checkPlayersArray = []

try:
    with open("players.txt", "r") as checkPlayersFile:
        for line in checkPlayersFile:
            tempPlayer, tempScore = line.split(" ")
            checkPlayersArray.append(tempPlayer)
    if (enteredPlayerName.title() or enteredPlayerName or enteredPlayerName.lower()) in checkPlayersArray:
        print("Authenticated!\n")
    else:
        print("Try again.")
        exit(0)
except FileNotFoundError:
  print("File 'players.txt' file not found, run the first option in the main options menu.\n")

# Function to add a user to the players file
def addingUser(toAppendName):
    with open("players.txt", "a+") as file_object:
      file_object.seek(0)
      data = file_object.read(100)
      if len(data) > 0 :
          file_object.write("\n")
      file_object.write(f"{toAppendName} 0")
      file_object.close()

# Main options loop
while True:
    choice = input("Enter an option to begin:\n1 - Adding User\n2 - Continue with existing files\ndone - Finished with this stage\nexit - Exit the program\n>>> ")
    if choice == "1":
        while True:
            # The'\033' makes the text inside them bold
            toAppendName = input("Enter the \033[1mname\033[0m of the new user (Enter \033[1m/done\033[0m to finish): ")
            if toAppendName == "/done":
                break
            addingUser(toAppendName)
    elif choice == "2":
        break
    elif choice == "done":
        break
    elif choice == "exit":
        print("Quitting...")
        exit(0)
    else:
        print("Invalid choice")
        break
