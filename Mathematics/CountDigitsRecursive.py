# Find the number of digits in a given number with a recursive solution.

def countDigits(num):
    if (num == 0):
        return 0
    else:
        return (1 + countDigits(num // 10))


num = int(input("Enter a Number:"))
print("No. of digits in given number is ", countDigits(num))

# Time Complexity - O(d) where, d is no. of digits in the given input.
