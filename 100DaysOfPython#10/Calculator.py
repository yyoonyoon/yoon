from Calculator_art import logo

def calculate(operation):
    global result
    if operation == "+":
        result = first_number + second_number
        print("{0} + {1} = {2}".format(first_number,second_number,result))
    elif operation == "-":
        result = first_number - second_number
        print("{0} - {1} = {2}".format(first_number,second_number,result))
    elif operation == "*":
        result = first_number * second_number
        print("{0} * {1} = {2}".format(first_number,second_number,result))
    elif operation == "/":
        result = first_number / second_number
        print("{0} / {1} = {2}".format(first_number,second_number,result))
print(logo)
first_number = float(input("What's the first number? : "))
result = 0

while True:
    print("+\n-\n*\n/")
    operation = input("Pick an operation : ")
    second_number = float(input("What's the second number? : "))
    calculate(operation)
    choice = input("Type 'y' to continue calculating with '{0}', or type 'n' to start new calculation or type any keys to end program : ".format(result))
    if (choice == "y"):
        first_number = result
    elif (choice == "n"):
        first_number = float(input("What's the first number? : "))
    else:
        break
