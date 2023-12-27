class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return (0)
        if n==1:
            return(1)
        def fibon(n):
            if n==0:
                return (0)
            if n==1:
                return (1)
            
            fib_n = fibon(n-1) + fibon(n-2)
            return (fib_n)
        return(fibon(n))
        