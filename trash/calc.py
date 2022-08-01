def add(x, y):
    return x+y

def multiply(x, y):
    return x*y

def divide(x, y):
    return x/y

def subtract(x, y):
    return x-y

def coreCalc(userOperator, userInputA, userInputB):
    match userOperator:
        case "+":
            return add(userInputA, userInputB)
        case "-":
            return subtract(userInputA, userInputB)
        case "*":
            return multiply(userInputA, userInputB)
        case "/":
            return divide(userInputA, userInputB)
        case _:
            return "you're an idiot"
# Main
def main():
    userOperator = input("Enter an operator (+, -, *, /): ")
    userInputA = int(input("Enter first number: "))
    userInputB = int(input("Enter second number: "))
    print(coreCalc(userOperator, userInputA, userInputB))
main()