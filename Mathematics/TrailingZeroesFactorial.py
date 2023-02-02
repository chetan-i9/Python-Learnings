# find a solution to count the number of trailing zeroes in a factorial of a given number.
# This is a naive solution.
def countzeroes(num):
    fact = 1
    for i in range(2, num + 1):
        fact = fact * i
    res = 0
    while (fact % 10 == 0):
        res += 1
        fact = fact // 10
    return res

num = int(input("Enter a number:"))
print("No. of Trailing Zeroes in the factorial of given number is ", countzeroes(num))

# Time Complexity - O(n)
