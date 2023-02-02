# Find the HCF or GCD of the given numbers.

def gcd(num1, num2):
    res = min(num1, num2)
    while (res > 0):
        if (num1 % res == 0) and (num2 % res == 0):
            break
        res -= 1
    return res

# Numbers entered should be separated with a single space.
num1, num2 = map(int, input("Enter two numbers:").split())
print("GCD or HCF of iven two numbers is ", gcd(num1, num2))

# Time Complexity - O(min(num1,num2))
