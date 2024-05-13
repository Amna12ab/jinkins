def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

# Get user input for the number
try:
    number = int(input("Enter a non-negative integer to calculate its factorial: "))
    if number < 0:
        raise ValueError("Please enter a non-negative integer.")
except ValueError as e:
    print(e)
else:
    result = factorial(number)
    print(f"The factorial of {number} is {result}")
