def get_factorial(num: int) -> int:         # using recursion
    if num == 0:
        return 1
    return get_factorial(num - 1) * num


try:
    number = int(input("Enter a number to find its factorial : "))
    print(f"The factorial of {number} is : ", get_factorial(number))
except ValueError:
    print("Invalid input. Enter only integer")
