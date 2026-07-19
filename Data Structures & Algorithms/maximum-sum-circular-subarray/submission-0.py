class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        maxx=float('-inf')
        globmaxx=float('-inf')
        minn=float('inf')
        globminn=float('inf')
        total=0
        for n in nums:
            total+=n
            maxx=max(maxx+n,n)
            globmaxx=max(globmaxx,maxx)
            minn=min(minn+n,n)
            globminn=min(minn,globminn)
        if globmaxx<0:
            return globmaxx
        else:
            return max(total-globminn,globmaxx)