# Slightly Complex Python Program: Check if a number is prime

def is_prime(number):
    # Prime numbers are greater than 1
    if number <= 1:
        return False
    # Check for factors
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is prime and print result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
