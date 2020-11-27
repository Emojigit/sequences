import math, sys

class SequenceInterrupt(BaseException):
    def __init__(self,reason=None):
        if reason == None:
            msg = "Sequence calcuate interrupted!"
        else:
            msg = "Sequence calcuate interrupted because "+reason
        print(msg)

mpow = math.pow
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
    fn = float(n)
    if n > 30:
        print("Calcuate Fibonacci Sequence needs some times. Please wait...")
    try:
        return fib(fn)
    except RecursionError:
        raise SequenceInterrupt("maximum recursion depth exceeded in comparison! (max:"+str(sys.getrecursionlimit())+")")

def pentagonal(n):
    fn = float(n)
    return (3*mpow(fn,2)-fn)/(2)

def hexa(n):
    return n*((2*n)-1)

# def caterer(n): Nedds fix
#     nf = float(n)
#     return (mpow(n,2)+n+2)/(2)

def wdemlo(n):
    # OEIS A002477
    fn = float(n)
    return mpow(((mpow(10,n)-1)/9),2)

def pow2(n):
    return mpow(n,2)

def div2(n):
    if n==1:
        return 1
    else:
        return div2(n-1)/2

def div2_exec(n):
    #if (n-5) > sys.getrecursionlimit():
    #    raise SequenceInterrupt()
    try:
        return div2(n)
    except RecursionError:
        raise SequenceInterrupt("maximum recursion depth exceeded in comparison! (max:"+str(sys.getrecursionlimit())+")")



# Register sequences
seqs = {
    "ODD":odd,
    "EVEN":even,
    "SQUARE":sq,
    "SQ":sq,
    "TRIANGULAR":trian,
    "TRIAN":trian,
    "FIB":fib_exec,
    "FIBONACCI":fib_exec,
    "PENTAGONAL":pentagonal,
    "PENT":pentagonal,
    "HEX":hexa,
    "HEXAGONAL":hexa,
    # "LAZYC":caterer,
    # "CATERER":caterer,
    "WDEMLO":wdemlo,
    "POW2":pow2,
    "DIV2":div2_exec
}

def ah(s):
    return "Same as "+s

helps = {
    "ODD":"Odd numbers",
    "EVEN":"Even numbers",
    "SQUARE":"Square numbers",
    "SQ":ah("SQUARE"),
    "TRIANGULAR":"Triangular numbers",
    "TRIAN":ah("TRIANGULAR"),
    "FIB":"Fibonacci sequences",
    "FIBONACCI":ah("FIB"),
    "PENTAGONAL":"Pentagonal numbers",
    "PENT":ah("PENTAGONAL"),
    "HEX":ah("HEXAGONAL"),
    "HEXAGONAL":"Hexagonal numbers",
    # "LAZYC":"WIP",
    # "CATERER":ah("LAZYC"),
    "WDEMLO":"Wonderful Demlo numbers (OEIS A002477)",
    "POW2":"Power of 2 (OEIS A000079)",
    "DIV2":"Dividing by 2"
}
