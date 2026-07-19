class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx=1
        minn=1
        result=max(nums)
        #(+,+) or (-,-) or (-,+)
        for num in nums:
            if num==0:
                maxx=1
                minn=1
            else:
                tmp=maxx*num
                maxx=max(tmp,minn*num,num)
                minn=min(tmp,minn*num,num)
                result=max(result,maxx)
        return result