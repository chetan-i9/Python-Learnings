# Find the number of digits in a given number with an iterative solution.

def countDigits(num):
    count: int = 0
    while (num != 0):
        num = num // 10
        count += 1
    return count


num = int(input("Enter a Number:"))
print("No. of digits in given number is ", countDigits(num))

# Time Complexity - O(d) where, d is no. of digits in the given input.
