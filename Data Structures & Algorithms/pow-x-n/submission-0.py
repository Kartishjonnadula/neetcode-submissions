class Solution:
    def myPow(self, x: float, n: int) -> float:
        def helper(n,x):
            if n==0:
                return 1
            if n==1:
                return x
            res=helper(n//2,x)
            if n%2==0:
                return res*res
            return res*res*x
        if n < 0:
            return 1 / helper(abs(n),x)
        return helper(n,x)
        