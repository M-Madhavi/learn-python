'''
fib(0) = 0
fib(1) = 1
fib(2) = fib(0)+fib(1)

fib(n) = fib(n-2)+fib(n-1)
'''
def fibo(n):
    if(n == 0 or n==1):
        return 1
    return fibo(n-2)+fibo(n-1)


print(fibo(6))


# factorial

def factorial(n):
    if(n== 0 or n==1):
        return 1
    return n*factorial(n-1)

print(factorial(5))