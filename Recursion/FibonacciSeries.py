def FibonacciSeries(n):
    if n==0 or n==1:
        return n
    return FibonacciSeries(n-1)+FibonacciSeries(n-2)