class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=1
        minn=1
        result=nums[0]
        for n in nums:
            tmp=maxx*n
            maxx=max(tmp,minn*n,n)
            minn=min(minn*n,tmp,n)
            result=max(maxx,result)
        return result
