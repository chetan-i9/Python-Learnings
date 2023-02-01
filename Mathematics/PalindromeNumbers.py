# Find whether a given number is a palindrome number or not.

def isPalindrome(num):
    rev = 0
    temp = num
    while (temp != 0):
        ld = temp % 10
        rev = rev * 10 + ld
        temp = temp // 10
    return (rev == num)


num = int(input("Enter a Number:"))
if (isPalindrome(num) == True):
    print("The given number is a Palindrome Number.")
else:
    print("The given number is not a Palindrome Number.")

# Time Complexity - O(d) where, d is no. of digits in the given number.
