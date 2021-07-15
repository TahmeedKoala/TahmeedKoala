calculator_use = input("Do you want to use the calculator?\nType yes/no: ")
if calculator_use == "yes":
    num1 = float(input("Enter first number: "))
    operator = input("Enter Operator: ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        print(num1 + num2)
    elif operator == "-":
        print(num1 - num2)
    elif operator == "/":
        print(num1 / num2)
    elif operator == "*":
        print(num1 * num2)
    else:
        print("Invalid Operator")
elif calculator_use == "no":
    game = input("Do you want to play the Guessing Game?\nType yes/no: ")
    if game == "yes":
        secret_num = 6
        guess_count = 0
        guess_limit = 3
        guess = ""
        out_of_guessess = False


        secret_num1 = 17
        guess_count1 = 0
        guess_limit1 = 3
        guess1 = ""
        out_of_guessess1 = False


        while guess != secret_num and not(out_of_guessess):
            if guess_count < guess_limit:
                guess = int(input("Enter a number out of 30: "))
                guess_count += 1
            else:
                out_of_guessess = True

        if out_of_guessess:
            print("Out of guesses!")
        else:
            print("You win!!")


        again = input("Do you want to play again?\nType yes/no:")

        if again == "yes":
            while guess1 != secret_num1 and not(out_of_guessess1):
                if guess_count1 < guess_limit1:
                    guess1 = int(input("Enter a number out of 30: "))
                    guess_count1 += 1
                else:
                    out_of_guessess1 = True

            if out_of_guessess1:
                print("Out of guesses!")
            else:
                print("You win!!")

        else:
            print("Thank you for playing!")
    else:
        print("Thank you for doing nothing!!")