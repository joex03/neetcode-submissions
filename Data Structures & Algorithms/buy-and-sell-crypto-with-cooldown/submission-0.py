class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mapper={}
        def helper(i,state):
            if i >=len(prices):
                return 0
            if (i,state) in mapper:
                return mapper[(i,state)]
            cool=helper(i+1,state)
            if state: #buying
                buy=helper(i+1,False)-prices[i]
                mapper[(i,state)]=max(buy,cool)
            else: # selling
                sell=helper(i+2,True)+prices[i]
                mapper[(i,state)]=max(sell,cool)
            return mapper[(i,state)]

        helper(0,True)
        return mapper[(0,True)]

