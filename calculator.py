import colorama
import inquirer
from colorama import Fore

# Welcoming User
print(Fore.MAGENTA + "Calculator App")
print("")

import inquirer
questions = [
  inquirer.List('option',
                message="Chosse which operation you want to do",
                choices=['Add', 'Subtract', 'Multiply', 'Divide'],
        ),
]

option = inquirer.prompt(questions)["option"]

firstnum = float(input(Fore.CYAN + "Enter first number: " + Fore.RESET))
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


if (option == 'Add'):
    add()
elif (option == 'Subtract'):
    subtract()
elif (option == 'Multiply'):
    multiplication()
elif (option == 'Divide'):
    divide()