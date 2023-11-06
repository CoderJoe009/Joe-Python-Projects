import math

def main():
    try:
        number = float(input('Give me a number: '))
        operation = input("Do you want to square, square root, take the logarithm, raise to a power, or perform a basic operation (+, -, *, /)? ").lower().strip()
        
        if operation.startswith("root"):
            sqroot = math.sqrt(number)
            print(f"The square root of {number} is {format_result(sqroot)}")
        elif operation.startswith("sq"):
            print(f"The square of {number} is {format_result(square(number))}")
        elif operation.startswith("log"):
            loga = math.log(number)
            print(f"The natural logarithm of {number} is {format_result(loga)}")
        elif operation.startswith("pow"):
            p = int(input("What's the power? "))
            print(f"{number} raised to the power {p} is {format_result(power(number, p))}")
        elif operation in ["+", "-", "*", "/"]:
            c = float(input("Enter the second number: "))
            if operation == "+":
                result = number + c
            elif operation == "-":
                result = number - c
            elif operation == "*":
                result = number * c
            elif operation == "/":
                if c == 0:
                    print("Division by zero is not allowed.")
                    return
                result = number / c
            print(f"The result of {number} {operation} {c} is {format_result(result)}")
        else:
            print("Enter a valid operation")
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def square(n):
    return pow(n, 2)

def power(n, p):
    return pow(n, p)

def format_result(result):
    if result.is_integer():
        return str(int(result))
    return f"{result:.3f}"

if __name__ == "__main__":
    main()


