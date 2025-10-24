def is_palindrome(number):
    original_number = number
    reversed_number = 0
    while number > 0:
        digit = number % 10
        reversed_number = reversed_number * 10 + digit
        number //= 10
    return original_number == reversed_number

def count_digits(number):
    digits_count = [0] * 10
    while number > 0:
        digit = number % 10
        digits_count[digit] += 1
        number //= 10
    return digits_count  # Moved outside the while loop

try:
    num = int(input("Enter a positive integer: "))
    if num < 0:
        print("Please enter a positive integer.")
    else:
        if is_palindrome(num):
            print(f"{num} is a palindrome.")
        else:
            print(f"{num} is not a palindrome.")
        digit_counts = count_digits(num)
        print("Digit counts:")
        for digit, count in enumerate(digit_counts):
            if count > 0:
                print(f"Digit {digit}: appears {count} time(s)")
except ValueError:
    print("Invalid input. Please enter a valid positive integer.")