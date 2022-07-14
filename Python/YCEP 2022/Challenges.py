# Challenge 1 (Calculator)

def addition():
     print("___ + ___")
     numA = int(input("First number: "))
     numB = int(input("Second number: "))
     print(f"Your result is {numA + numB}")

def subtraction():
     print("___ - ___")
     numA = int(input("First number: "))
     numB = int(input("Second number: "))
     print(f"Your result is {numA - numB}")

def multiplication():
     userInput2 = int(input("Select an option:\n1) Simple multiplication\n2) Indices/Exponents\nOption: "))
     if userInput2 == 1:
         print("___ * ___")
         numA = int(input("First number: "))
         numB = int(input("Second number: "))
         print(f"Your result is {numA*numB}")
     elif userInput2 == 2:
         print("___^___")
         numA = int(input("First number: "))
         numB = int(input("Second number: "))
         print(f"Your result is {numA**numB}")
     else:
         print("Error! Please put in a valid number.")

def division():
     userInput3 = int(input("Select an option:\n1) Simple division (Get exact value)\n2) Get the whole number (Skip remainder)\n3) Get the remainder\nOption: "))
     if userInput3 == 1:
         print("___ ÷ ___")
         numA = int(input("First number: "))
         numB = int(input("Second number: "))
         print(f"Your result is {numA/numB}")
     elif userInput3 == 2:
         print("___ ÷ ___")
         numA = int(input("First number: "))
         numB = int(input("Second number: "))
         print(f"Your result is {numA//numB}")
     elif userInput3 == 3:
         print("___ ÷ ___")
         numA = int(input("First number: "))
         numB = int(input("Second number: "))
         print(f"Your result is {numA%numB}")
     else:
         print("Error! Please put in a valid number.")

UserInput = input("Select a function: \n1) (+) Addition\n2) (-) Subtraction\n3) (*) Multiplication\n4) (÷) Division\nOption: ")

if UserInput == "1":
     addition()
elif UserInput == "2":
     subtraction()
elif UserInput == "3":
     multiplication()
elif UserInput == "4":
     division()
else:
     print("Error! Please put in a valid number.")

# Challenge 2 (The odd or even definitor)

# Challenge 3 (Rock Paper Scissors)

import random

robotChoice = random.randint(1,3)
weapon = ""
if robotChoice == 1:
    weapon = "rock"
elif robotChoice == 2:
    weapon = "paper"
else:
    weapon = "scissors"

userChoice = int(input("Choose your weapon:\n1) Rock\n2) Paper\n3) Scissors\nOption: "))

def playerChooseRock():
    if weapon == "rock":
        print("The robot chose rock. It was a tie.")
    elif weapon == "paper":
        print("The robot chose paper. You lost.")
    elif weapon == "scissors":
        print("The robot chose scissors. You won!")

def playerChoosePaper():
    if weapon == "paper":
        print("The robot chose paper. It was a tie.")
    elif weapon == "scissors":
        print("The robot chose scissors. You lost.")
    elif weapon == "rock":
        print("The robot chose rock. You won!")

def playerChooseScissors():
    if weapon == "scissors":
        print("The robot chose scissors. It was a tie.")
    elif weapon == "rock":
        print("The robot chose rock. You lost.")
    elif weapon == "paper":
        print("The robot chose paper. You won!")

if userChoice == 1:
    playerChooseRock()
elif userChoice == 2:
    playerChoosePaper()
elif userChoice == 3:
    playerChooseScissors()
else:
    print("Invalid choice")
