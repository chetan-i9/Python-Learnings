# Find a solution that checks whether a number is a prime number or not.
# This is an efficient solution.

def check_prime(num):
    if (num == 1):
        return False
    i = 2
    while (i * i <= num):
        if (num % i == 0):
            return False
        i += 1
    return True

num = int(input("Enter a Number:"))
if not check_prime(num):
    print("The given number is not a Prime Number.")
else:
    print("The given number is a Prime Number.")

# Time Complexity - O(√n)
