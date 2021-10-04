from colors import bcolors
import inquirer

# Welcoming User
print(bcolors.HEADER + "Calculator App")
print("")

import inquirer
questions = [
  inquirer.List('option',
                message="Chosse which operation you want to do",
                choices=['Add', 'Subtract', 'Multiply', 'Divide'],
        ),
]

option = inquirer.prompt(questions)["option"]

firstnum = float(input(bcolors.OKCYAN + "Enter first number: " + bcolors.ENDC))
secondnum = float(input((bcolors.OKCYAN + "Enter second number: " + bcolors.ENDC)))


# addition 
def add():
    print(bcolors.HEADER + "You have selected addition")
    result4add = firstnum + secondnum
    print(bcolors.OKGREEN + "Your result is: ", result4add)

# subtraction
def subtract():
    print(bcolors.HEADER + "You have selected Subtraction")
    result4sub = firstnum - secondnum
    print(bcolors.OKGREEN + "Your result is: ", result4sub)


# multiplication 
def multiplication():
    print(bcolors.HEADER + "You have selected Multiplication")
    result4multipy = firstnum * secondnum
    print(bcolors.OKGREEN + "Your result is: ", result4multipy)

# divide
def divide():
    print(bcolors.HEADER + "You have selected Division")
    result4div = firstnum / secondnum
    print(bcolors.OKGREEN + "Your result is: ", result4div)


if (option == 'Add'):
    add()
elif (option == 'Subtract'):
    subtract()
elif (option == 'Multiply'):
    multiplication()
elif (option == 'Divide'):
    divide()