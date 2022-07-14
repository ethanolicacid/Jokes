def addition(numA, numB):
    result = numA + numB
    return result


def subtraction(numA, numB):
    user_input = input(f"Do you want:\n1) {numA} - {numB} \n2){numB} - "
                       f"{numA}\n Answer (1/2): ")
    result1A = numA - numB
    result1B = numB - numA
    if user_input == "1":
        return result1A
    elif user_input == "2":
        return result1B
    else:
        print("Invalid choice")


def multiplication(numA, numB):
    result2 = numA * numB
    return result2


def division(numA, numB):
    user_input1 = input("Do you want: \n1) Regular division\n2) Whole number "
                        "with remainder \n Answer (1/2): ")
    if user_input1 == "1":
        user_input1A = input(f"Do you want: \n1) {numA} ÷ {numB}\n2) "
                             f"{numB} ÷ {numA}\nAnswer (1/2): ")
        if user_input1A == "1":
            result3A = numA / numB
            return result3A
        elif user_input1A == "2":
            result3B = numB / numA
            return result3B
        else:
            print("Invalid choice")

    elif user_input1 == "2":
        user_input1B = input(f"Do you want: \n1) {numA} ÷ {numB}\n2) "
                             f"{numB} ÷ {numA}\nAnswer (1/2): ")
        if user_input1B == "1":
            result3C = numA // numB
            result3D = numA % numB
            final_result1A = str(result3C) + "R" + str(result3D)
            print(final_result1A)
        elif user_input1B == "2":
            result3E = numB // numA
            result3F = numB % numA
            final_result1B = str(result3E) + "R" + str(result3F)
            print(final_result1B)
        else:
            print("Invalid choice")


def exponent(numA, numB):
    user_input2 = input(f"Do you want:\n1) {numA}^{numB}\n2) {numB}^"
                        f"{numA}\nAnswer (1/2): ")
    if user_input2 == "1":
        result4A = numA ** numB
        return result4A
    elif user_input2 == "2":
        result4B = numB ** numA
        return result4B
    else:
        print("Invalid choice")


user_input3 = int(input("Hello there, which operation would you like to "
                        "use?\n1) "
                        "Addition\n2) Subtraction \n3) Multiplication \n4) "
                        "Division\n5) Exponent\nAnswer with the representing numeral: "))
numA = int(input("Type in your first number: "))
numB = int(input("Type in your second number: "))

if user_input3 == 1:
    print(addition(numA, numB))
elif user_input3 == 2:
    print(subtraction(numA, numB))
elif user_input3 == 3:
    print(multiplication(numA, numB))
elif user_input3 == 4:
    division(numA, numB)
elif user_input3 == 5:
    print(exponent(numA, numB))
else:
    print("Invalid choice")