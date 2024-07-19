class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            fi = 0
            return fi
        if n==1:
            fi =1
            return fi
        fib_n = self.fib(n-1) + self.fib(n-2)
        return (fib_n)
#         a=[]
#         a.append(0)
#         a.append(1)

#         for i in range(2,n+1):
#             a.append(a[n-1]+a[n-2])
#         return(a[n])
        