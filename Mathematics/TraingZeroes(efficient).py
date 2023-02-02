# find a solution to count the number of trailing zeroes in a factorial of a given number.
# This is an efficient solution.
def countzeroes(num):
    count = 0
    i = 5
    while (num / i >= 1):
        count += int(num / i)
        i *= 5
    return int(count)

num = int(input("Enter a number:"))
print("No. of Trailing Zeroes in the factorial of given number is ", countzeroes(num))

# Time Complexity - O(logn)
