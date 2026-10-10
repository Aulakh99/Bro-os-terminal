

def run_calculator():
    print("--- Calculator App ---")
    
    # Simple example calculation
    try:
        num1 = float(input("Enter first number: "))
        op = input("Enter operator (+, -, *, /): ")
        num2 = float(input("Enter second number: "))

        if op == "+":
            print(f"Result: {num1 + num2}")
        elif op == "-":
            print(f"Result: {num1 - num2}")
        elif op == "*":
            print(f"Result: {num1 * num2}")
        elif op == "/":
            print(f"Result: {num1 / num2}")
        else:
            print("Invalid operator!")
    except ValueError:
        print("Invalid number input!")