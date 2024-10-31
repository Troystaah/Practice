result = 0 
# define function for calculator
def calculator():
    # setting validOperation with mathematical operators within list. 
    valid_operation = ["*","+","-","/"]
    # ask user for first number and convert from string to float
    # while loop is error checking for any input that is not a number
    while True:
        try:
            x = float(input("Enter first number: "))
            break
        except ValueError: 
            print("Invalid input. Please enter a number.")
    # ask user for operation they would like to perform
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in valid_operation:
            break
        else:
            print("Error, invalid operation")
    # ask user for second number and convert from string to float
    # setting y = 0 so that while loop can function below
    # while loop tests for division by 0 and returns error msg if user is trying to do so and also error checks for input that is not a number. 
    y = 0                                                                   
    while y == 0:
        try:
            y = float(input("Enter second number: "))
            if operation == "/" and y == 0:
                print("Cannot divide by 0")
        except ValueError: 
            print("Invalid input. Please enter a number.")
    # perform mathemathical operation based on user selection
    if operation == "+":
        result = x + y 
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        result = x / y 
    else:
        result = "Error: Invalid Operation"
    # print the result
    print(result)
    # calling the calculator function
    return result

# new calculator function for storing and operating on last result
def calculator_2(result):
    valid_operation = ["*","+","-","/"]
    x = result
    while True:
        operation = input("Choose an operation (+, -, *, /): ")
        if operation in valid_operation:
            break
        else:
            print("Error, invalid operation")
    y = 0
    while y == 0:
        try:
            y = float(input("Enter second number: "))
            if operation == "/" and y == 0:
                print("Cannot divide by 0")
        except ValueError: 
            print("Invalid input. Please enter a number.")
    # perform mathemathical operation based on user selection
    if operation == "+":
        result = x + y 
    elif operation == "-":
        result = x - y
    elif operation == "*":
        result = x * y
    elif operation == "/":
        result = x / y 
    else:
        result = "Error: Invalid Operation"
    print(result)
    return result

def main():
    user_input = input("Would you like to exit? (Y/N)").lower()
    while user_input == "n":
        last_result = calculator()
        user_input = input("Would you like to exit? (Y/N)").lower()
        while user_input == "n":
            last_result = calculator_2(last_result)
            user_input = input("Would you like to exit? (Y/N)").lower()

if __name__ == "__main__":
    main()