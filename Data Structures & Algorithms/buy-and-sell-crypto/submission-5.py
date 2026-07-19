class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxx,minn=0,prices[0]
        for i in range(0,len(prices)):
            minn=min(minn,prices[i])
            maxx=max(maxx,prices[i]-minn)
        return maxx