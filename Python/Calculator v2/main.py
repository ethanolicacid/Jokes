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
         print(f"Your result is {numA%numB}2")
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
