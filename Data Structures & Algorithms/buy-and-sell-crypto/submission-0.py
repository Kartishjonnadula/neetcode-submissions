class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minsofar=prices[0]
        maxprofit=0
        for i in range(1,len(prices)):
            curr=prices[i]
            profit=curr-minsofar
            if curr<minsofar:
                minsofar=curr
            maxprofit=max(profit,maxprofit)
        return maxprofit
        