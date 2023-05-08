#Alexza Jean R. Catanoy
#BSCPE 1-4
#Exception Handling

#Title
print("\033[0;36m*" * 90)
print("\033[1;97mA Simple App Calculator with Appropriate Exception Handling".center(97))
print("\033[0;36m*" * 90)

print("\033[1;32m\nHello! Your programmers name is Alexza Jean.")
print("\033[1;32m\nShe's from BSCPE 1-4")
print("-" * 90)

def calculator():
    try:
        #Let the user pick among the four math operations
        math_operation = input("Hi my friend! Kindly pick one math operation among these four (+, -, *, /): ")

        #Let the user type in two numbers
        num1 = float(input("Kindly type in the first number you like: "))
        num2 = float(input("KIndly type in the second number you like: "))

        #Using the math operation that the user pick, execute the calculation

        #If +, add num1 and num2
        if math_operation == "+":
            output = num1 + num2

        #If -, subtract num1 and num2
        elif math_operation == "-":
            output = num1 - num2

        #If *, multiply num1 and num2
        elif math_operation == "*":
            output = num1 * num2

        #If /, divide num1 and num2
        elif math_operation == "/":
            output = num1 / num2

        else:
            raise ValueError("The operation you pick is not in the option.") 
        
        #Show the output of the program
        print("Output: ", output)

        #Ask the user if they want to try again for another operation and numbers
        option = input("Hi my friend! Would you like to try another operation and numbers? (yes/no): ")

        #If the user said yes, just repeat the whole process
        if option.lower() == "yes":
            calculator()

        #If the user said no, print "Thank you for using this simple app calculator I made." and then end program
        elif option.lower() == "no":
            print("Thank you for using this simple app calculator I made.")

        else:
            raise ValueError("The option you choose in not valid.")

    except (ValueError, ZeroDivisionError) as e:
        print("Exception: ", e)
        calculator()

calculator()