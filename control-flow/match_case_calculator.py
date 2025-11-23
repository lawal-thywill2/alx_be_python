Num1 = int(input("Enter the first number: "))
Num2 = int(input("Enter the second number: "))
operation = input("Choose the operation (+, -, *, /): ").strip()

match operation:
    case "+" :
        result = Num1 + Num2
        print(f"The result is: {result}")
    case "-" :
        result = Num1 - Num2
        print(f"The result is: {result}")
    case "*" :
        result = Num1 * Num2
        print(f"The result is: {result}")
    case "/" :
        if Num2 != 0:
            result = Num1 / Num2
            print(f"The result is: {result}")
        else:
            print("cannot divide by zero.")