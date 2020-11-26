import math
def odd(n):
    return (2*n)-1

def even(n):
    return 2*n

def sq(n):
    return math.pow(n,2)

def trian(n):
    return (n(n+1))/2

def fib(n): # This code is contributed by Saket Modi, https://www.geeksforgeeks.org/python-program-for-program-for-fibonacci-numbers-2/
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fib(n-1)+fib(n-2)

def fib_exec(n):
    if n > 30:
        print("Calcuate Fibonacci Sequence needs some times. Please wait...")
    return fib(n)

seqs = {
    "ODD":odd,
    "EVEN":even,
    "SQUARE":sq,
    "SQ":sq,
    "TRIANGULAR":trian,
    "TRIAN":trian,
    "FIB":fib_exec,
    "FIBONACCI":fib_exec,
}
