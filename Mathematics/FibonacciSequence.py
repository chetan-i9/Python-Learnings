# Find a solution to print a Fibonacci Sequence.

def fibonacci(num):
    num1 = 0
    num2 = 1
    count = 0
    if (num <= 0):
        print("Not Valid Input.")
    elif (num == 1):
        print(num1)
    else:
        print("Fibonacci Series:-", end=" ")
        while (count < num):
            print(str(num1), end=" ")
            sum = num1 + num2
            num1 = num2
            num2 = sum
            count += 1

num = int(input("Enter a Number:"))
fibonacci(num)
