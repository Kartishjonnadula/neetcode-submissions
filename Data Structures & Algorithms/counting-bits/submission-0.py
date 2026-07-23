class Solution:
    def countBits(self, n: int) -> List[int]:
        dp=[0]*(n+1)
        def solve(n):
            if n in dp:
                return dp[n]
            if n==0:
                dp[0]=0
                return 0
            dp[n]=solve(n>>1) + (1&n)
            return dp[n]
        # for i in rangen+1,-1,-1):
            # if i not in dp:
                # solve(i)

        # print(dp)
        # return [dp[i] for i in range(n+1)]
        # dp[0]=0
        for i in range(1,n+1):
            dp[i]=dp[i>>1]+(1&i)
        return dp