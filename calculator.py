import sys

def multiply_numbers(num1, num2):
    return num1 * num2

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python program.py <number1> <number2>")
        sys.exit(1)

    try:
        num1 = float(sys.argv[1])
        num2 = float(sys.argv[2])
    except ValueError:
        print("Error: Please provide valid numbers")
        sys.exit(1)

    result = multiply_numbers(num1, num2)
    print("Result:", result)
