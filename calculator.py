# Welcoming User
print("Calculator App")
print("")
# Chosse Option
print("Chosse which operation you want to do")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("select from '1', '2', '3', '4'")

selectOption = input("Please select one of the option ")


firstnum = float(input("Enter first number "))
secondnum = float(input("Enter second number "))


# addition 
def add():
    print("You have selected addition")
    result4add = firstnum + secondnum
    print("Your result is: ", result4add)

# subtraction
def subtract():
    print("You have selected Subtraction")
    result4sub = firstnum - secondnum
    print("Your result is: ", result4sub)


# multiplication 
def multiplication():
    print("You have selected Multiplication")
    result4multipy = firstnum * secondnum
    print("Your result is: ", result4multipy)

# divide
def divide():
    print("You have selected Division")
    result4div = firstnum / secondnum
    print("Your result is: ", result4div)


if (selectOption == '1'):
    add()
elif (selectOption == '2'):
    subtract()
elif (selectOption == '3'):
    multiplication()
elif (selectOption == '4'):
    divide()
else:
    print("Error! please select suitable option")