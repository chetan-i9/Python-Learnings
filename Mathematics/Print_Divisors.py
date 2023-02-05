# Find a solution that can print all the divisors of a given number.
# This is a Naive Solution.

def print_divisors(num):
    for i in range(1,num + 1):
        if (num % i == 0):
            print(str(i), end=" ")


num = int(input("Enter a Number:"))
print("Divisors of a given number are: ")
print_divisors(num)

# Time Complexity - O(n)
# Auxiliary Space - O(1)
