class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx,minn=1,1
        result=max(nums)
        for num in nums:
            if num==0:
                maxx,minn=1,1
            # handle the (+,+)&(-,-)&(+,-)
            tmp=num*maxx
            maxx=max(num*maxx,num*minn,num)
            minn=min(tmp,num*minn,num)
            result=max(result,maxx)
        return result