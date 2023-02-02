# Find the HCF or GCD of the given numbers.
# This program uses optimized implementation of Euclid's Algorithm.

def gcd(num1, num2):
    if (num2 == 0):
        return num1
    else:
        return gcd(num2, num1 % num2)

# Numbers entered should be separated with a single space.
num1, num2 = map(int, input("Enter two numbers:").split())
print("GCD or HCF of given two numbers is ", gcd(num1, num2))

# Time Complexity - O(log(min(num1,num2)))
