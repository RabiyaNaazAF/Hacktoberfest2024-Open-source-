def is_whole_number(num):
    return isinstance(num, int) and num >= 0

# Get user input
user_input = input("Enter a number: ")

try:
    # Try to convert input to an integer
    number = int(user_input)
    if is_whole_number(number):
        print(f"{number} is a whole number.")
    else:
        print(f"{number} is not a whole number.")
except ValueError:
    print("Please enter a valid number.")
