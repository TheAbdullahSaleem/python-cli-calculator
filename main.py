def addition(num1,num2):
    print(f"Your answer is {num1 + num2}")
def substraction(num1,num2):
    print(f"Your answer is {num1 - num2}")
def multiplication(num1,num2):
    print(f"Your answer is {num1 * num2}")
def division(num1,num2):
    try:
        print(f"Your answer is {num1 / num2}")
    except ZeroDivisionError:
        print("Sorry but you cannot divide any number with zero")
def power(num1,num2):
    print(f"Your answer is {num1 ** num2}")
def modulus(num1,num2):
    try:
        print(f"Your answer is {num1 % num2}")
    except ZeroDivisionError:
        print("Sorry but you cannot find modulus of zero any number with zero")
def operation_input():
    while True:
        while True:
            try:
                operation = int(input("""Enter the opertion according to listing
1:Addition
2:Substraction
3:Multiplication
4:Division
5:Power
6:Modulus
7:Quit:       """))
            except ValueError:
                print("Please only enter a \nnumber not anything else")
            else:
                break
        if operation < 1 or operation > 7:
            print("Please enter a valid choice")
            continue
        else:
            break
    return(operation)
def nums_input():
    while True:
        try:
            num1 = float(input("Enter the first number for calculations:    "))
        except ValueError:
            print("Please only enter a \nnumber not anything else")
        else:
            break
    while True:
        try:
            num2 = float(input("Enter the second number for calculations:    "))
        except ValueError:
            print("Please only enter a \nnumber not anything else")
        else:
            break
    return(num1,num2)
def calculator():
    while True:
        operation = operation_input()
        if operation == 7:
            print("Goodbye!")
            break
        num1 , num2 = nums_input()
        if operation == 1:
            addition(num1,num2)
        elif operation == 2:
            substraction(num1,num2)
        elif operation == 3:
            multiplication(num1,num2)
        elif operation == 4:
            division(num1,num2)
        elif operation == 5:
            power(num1,num2)
        elif operation == 6:
            modulus(num1,num2)

calculator()