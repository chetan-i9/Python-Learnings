# Find a solution that checks whether a number is a prime number or not.
# This is a naive solution.

def check_prime(num):
    if (num == 1):
        return False
    for i in range(2, num):
        if (num % i == 0):
            return False
    return True

num = int(input("Enter a Number:"))
if not check_prime(num):
    print("The given number is not a Prime Number.")
else:
    print("The given number is a Prime Number.")

# Time Complexity - O(√n)
