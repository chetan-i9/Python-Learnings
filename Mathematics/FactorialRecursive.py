#find a recursive solution for a factorial of a number

def factorial(num):
    if (num==0):
        return 1
    return num*factorial(num-1)

num=int(input("Enter a Number:"))
print("Factorial of the given number is ",factorial(num))

#Time Complexity - O(n)
#Auxilary Space - O(n) because of (n+1) recursive calls in stack.