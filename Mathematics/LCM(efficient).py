# Find LCM of given two numbers
# This is an efficient solution.

def gcd(num1, num2):
    if (num2 == 0):
        return num1
    return gcd(num2, num1 % num2)

def lcm(num1, num2):
    return (num1 * num2) / gcd(num1, num2)

# Numbers entered should be separated with a single space.
num1, num2 = map(int, input("Enter two numbers:").split())
print("LCM of given two numbers is ", lcm(num1, num2))

# Time Complexity - O(log(min(num1,num2)))
