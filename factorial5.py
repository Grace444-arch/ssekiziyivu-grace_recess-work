number = 5
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
factorial_result = factorial(number)
print(f"The factorial of {number} is {factorial_result}")  # Output: The factorial of 5 is 120

# Assignment two: Write a program to handle errors, the program should ask for two numbers using input and
# then divides them. Use an infinite loop to keep asking until a valid input is provided.

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        result = num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by zero, please enter a valid second number.")
    except ValueError:
        print("Invalid input, please enter numeric values.")
    else:
        print(f"The result of dividing {num1} by {num2} is {result}")
        break
    finally:
        print("Attempt to divide completed.")