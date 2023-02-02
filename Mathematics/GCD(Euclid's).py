# Find the HCF or GCD of the given numbers.
# This program uses basic implementation of Euclids Algorithm.

def gcd(num1, num2):
    while (num1 != num2):
        if (num1 > num2):
            num1 -= num2
        else:
            num2 -= num1
    return num1


# Numbers entered should be separated with a single space.
num1, num2 = map(int, input("Enter two numbers:").split())
print("GCD or HCF of given two numbers is ", gcd(num1, num2))

# Time Complexity - O(log(min(num1,num2)))
