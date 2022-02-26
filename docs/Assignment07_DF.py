# ------------------------------------------------- #
# Title: Assignment07: Error handling and Pickle
# Description: Program that asks a user for a list of board games and the number of players that can play.
# ChangeLog: (Who, When, What)
# <Dan Ficek>,<2.25.2022>,Created Script
# ------------------------------------------------- #
import pickle # This imports code from another code file!

# -- Data -- #
# declare variables and constants
intId=0;    #number of players
strGameName=""  #game name
userChoice="Yes" #continue yes or no
lstGames=[] #list of games built by user


#----Main code section===#
print("Welcome to the board game decider!  This program will help you choose the best game to play  ")
print("Let's get started on building your list of games")

while (True):

    userChoice=input("Do you have more games to add?  Type 'Yes' to continue or 'No' to exit:")

    if userChoice.lower()=="yes":

        strGameName = str(input("Enter a board game title: "))

        try:
            intId = int(input("Enter a number of players: "))
            lstGames = [strGameName, intId]
            # Append the data to a pickled file with the pickle.dump method
            objFile = open("AppData.dat", "ab")
            pickle.dump(lstGames, objFile)
            objFile.close()

        except ValueError as e:
            print("Please only enter a whole number for number of players!")

        except Exception as e:
            print("There was a non-specific error!")
            print("Built-In Python error info: ")
        continue

    else:
        break
# And, we read the data back with the pickle.load method

objFile = open("AppData.dat", "rb")
print("Here's what the binary file contains:")

while(True):
    try:
        objFileData = pickle.load(objFile) #load() only loads one row of data.
        print(objFileData)
    except EOFError as e:
        print("Here's confirmation that all contents of file were loaded!")
        break
objFile.close()