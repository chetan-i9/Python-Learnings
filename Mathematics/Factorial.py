#find an iterative solution for a factorial of a number

def factorial(num):
    res=1
    for i in range(2,num+1):
        res=res*i
    return res

num=int(input("Enter a Number:"))
print("Factorial of the given number is ",factorial(num))

#Time Complexity - O(n)
#Auxilary Space - O(1) better than Recursive.