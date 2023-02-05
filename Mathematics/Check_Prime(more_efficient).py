# Find a solution that checks whether a number is a prime number or not.
# This is a more efficient solution.

def check_prime(num):
    if (num == 1):
        return False
    if (num == 2) or (num == 3):
        return True
    if (num % 2 == 0) or (num % 3 == 0):
        return False
    i = 5
    while (i * i <= num):
        if (num % i == 0) or (num % (i + 2) == 0):
            return False
        i += 6
    return True

num = int(input("Enter a Number:"))
if not check_prime(num):
    print("The given number is not a Prime Number.")
else:
    print("The given number is a Prime Number.")

# Time Complexity - O(√n)
