##Find the number of digits in a given number with a logarithmic solution.
import math
def countDigits(num):
    return math.floor(math.log10(num)+1)

num=int(input("Enter a Number:"))
print("No. of digits in given number is ",countDigits(num))

#Time Complexity - O(d) where, d is no. of digits in the given input.