class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        from functools import cache
        @cache
        def solve(amount,i):
            
            if amount==0:
                return 1
            if amount<0 or i>=len(coins):
                return 0
            return solve(amount-coins[i],i)+solve(amount,i+1)
        return solve(amount,0)