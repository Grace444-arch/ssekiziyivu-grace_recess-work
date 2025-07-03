def square(x):
    """
    This function takes an integer x and returns its square.
    """
    return x * x
print(square(5))  # Output: 25
add = lambda x, y: x + y
print(add(5, 3))  # Output: N
numbers = [1, 2, 3, 4, 5]
squared_numbers = list(map(lambda x: x ** x, numbers))
print(squared_numbers)  # Output: [1, 4, 27, 256, 3125]

numbers = [1, 2, 3, 4, 5]
factorial = lambda x: 1 if x == 0 else x * factorial(x - 1)
factorial_numbers = list(map(factorial, numbers))
print(factorial_numbers)  # Output: [1, 2, 6, 24, 120]

try:
    result = 5 / 2
except ZeroDivisionError :
  print("cannot divide by zero")
else:
    print("Division successful", result)
finally:
    print("run completed")
   
   #exercise Five: raise a custom exception that checks for postive numbers

try:
    number = int(input("Enter a positive number: "))
    if number < 0:
        raise ValueError("The number is not positive")
except ValueError as e:
    print(e)            
finally:
    print("Execution completed", number)  
    #assignment two:
    # write a program to handle errors, the program should ask for two numbers using input and 
    # then divides them.use an infinite loop to keep asking until  a valid input is provided.      
    