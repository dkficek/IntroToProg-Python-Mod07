Dan Ficek

February 26, 2022

Foundations of Programming

Assignment 07

[Github Link](https://github.com/dkficek/IntroToProg-Python-Mod07/)
# Pickling and Exception Handling

## Summary

In this module we learned how to use the Pickle function in Python.  To "Pickle" Means to perserve something, and it means 
the same thing in Python. It's a way of preserving information in a binary file for retreival at a later time. The difference
between Pickling and the "write" function in Python is whether the file gets coded in binary language or one that is legible 
to humans. 

## Assignment Exercise: Create a program that demonstrates pickling and exception handling

To demonstrate pickling and exception handling, I created a program that allows a user to build a list of games and the 
number of players that can play them.  The program initializes by first declaring the variables to be used, as shown below:

```
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
```

Once the variables are declared, the program begins a loop and menu where it asks a user to add games and the number of players to a list.
Here is where it makes use of exception handling:  if the user enters anything but an integer for the number of players, they get a nice Error message 
that tells them they need to enter a whole number only.  

```
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
```

Here's what it looks like when run in command window and the user enters a non-integer for the number of players:

![Player_error](https://user-images.githubusercontent.com/99514147/155855218-1cb1fa55-e6ec-46d6-bbdb-6d18f99730eb.png)

Note that, as the user continues to add games and players to the list, the program takes that information and appends it to a pickled file.  This is accomplished with 
this section of code:

```
# Append the data to a pickled file with the pickle.dump method
            objFile = open("AppData.dat", "ab")
            pickle.dump(lstGames, objFile)
            objFile.close()
```
Once the user is done entering their list, they enter anything other than "yes" to the prompt that asks them whether they'd like to continue entering games.  
When this happens, the code exits the loop.  It then enters a new loop to use the Pickle load function to load all of the contents of the pickled file and display
them to the user. The code is shown below:

```
while(True):
    try:
        objFileData = pickle.load(objFile) #load() only loads one row of data.
        print(objFileData)
    except EOFError as e:
        print("Here's confirmation that all contents of file were loaded!")
        break
objFile.close()
```

In command window this appears like this:

![final_display](https://user-images.githubusercontent.com/99514147/155855549-04b13ec8-d74a-4a37-bc5f-ebccd319e329.png)

Note that this piece of code also makes use of the concept of exception handling.  It uses a loop to continue loading rows of data from the
pickled file until there are no more.  When it's reached the last line of the file, instead of throwing an error, the error is handled by 
displaying a confirmation message that it loaded everything in the file! 

## Summary

In this module we learned the benefits of being able to make use of an existing Python function: Pickling. 
We also learned how to handle errors/exceptions using the try/except block so that users can get a friendly 
error message to help them understand where they went wrong.  We then posted our code into a GitHub Page and learned
a bit about the Markdown format to post our learning document in a nice format.  




