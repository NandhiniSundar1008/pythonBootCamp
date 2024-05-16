# while loop in Fibonacci return values
'''n = 10
first = 0
second = 1
i = 0
while i < n:
    print(first)
    fibonacci = first + second
    first = second
    second = 
    i += 1'''

0,1,2,3







'''# Recursion in Fibonacci return index
def fibonacci(n, first=0, second=1):
    if n == 0:
        return first
    elif n == 1:
        return second
    else:
        return fibonacci(n - 1, second, first + second) #Function call
print(fibonacci(10)) # main function call'''

#0,1,1,2,3,5,8,13,21,34,55


def fibonacci(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonacci (n-1) + fibonacci (n-2)
print(fibonacci(4))

