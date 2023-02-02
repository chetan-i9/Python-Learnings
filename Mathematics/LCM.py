# Find LCM of given two numbers
# This is a naive solution.

def lcm(num1, num2):
    res = max(num1, num2)
    while (True):
        if (res % num1 == 0) and (res % num2 == 0):
            return res
        res += 1

# Numbers entered should be separated with a single space.
num1, num2 = map(int, input("Enter two numbers:").split())
print("LCM of given two numbers is ", lcm(num1, num2))

# Time Complexity - O(num1*num2)
