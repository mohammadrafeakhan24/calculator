import colorama
import inquirer
from colorama import Fore
from math import factorial as _factorial

# Welcoming User
print(Fore.MAGENTA + "Calculator App")
print("")

import inquirer
questions = [
  inquirer.List('option',
                message="Chosse which operation you want to do",
                choices=['Add', 'Subtract', 'Multiply', 'Divide', 'Exponent', 'Factorial'],
        ),
]

option = inquirer.prompt(questions)["option"]

firstnum = float(input(Fore.CYAN + "Enter first number: " + Fore.RESET))
if not (option == 'Factorial'):  # Factorial requires only one number.
    secondnum = float(input((Fore.CYAN + "Enter second number: " + Fore.RESET)))


# addition 
def add():
    print(Fore.MAGENTA + "You have selected addition")
    result4add = firstnum + secondnum
    print(Fore.GREEN + "Your result is: ", result4add)

# subtraction
def subtract():
    print(Fore.MAGENTA + "You have selected Subtraction")
    result4sub = firstnum - secondnum
    print(Fore.GREEN + "Your result is: ", result4sub)


# multiplication 
def multiplication():
    print(Fore.MAGENTA + "You have selected Multiplication")
    result4multipy = firstnum * secondnum
    print(Fore.GREEN + "Your result is: ", result4multipy)

# divide
def divide():
    print(Fore.MAGENTA + "You have selected Division")
    result4div = firstnum / secondnum
    print(Fore.GREEN + "Your result is: ", result4div)

# Exponent
def exponent():
    print(Fore.MAGENTA + "You have selected Exponent")
    result4exp = firstnum**secondnum
    print(Fore.GREEN + "Your result is: ", result4exp)

# Factorial
def factorial():
    print(Fore.MAGENTA + "You have selected Factorial")
    try:
        result4facto = _factorial(firstnum)
        print(result4facto)
    except ValueError:
        print(Fore.RED + f"Error: Unable to find the factorial of {firstnum}. Make sure that {firstnum} is a whole number")


if (option == 'Add'):
    add()
elif (option == 'Subtract'):
    subtract()
elif (option == 'Multiply'):
    multiplication()
elif (option == 'Divide'):
    divide()
elif (option == 'Exponent'):
    exponent()
elif (option == 'Factorial'):
    factorial()
