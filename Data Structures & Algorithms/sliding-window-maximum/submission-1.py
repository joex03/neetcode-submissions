class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l=0
        r=k-1
        result=[]
        maxx=float('-inf')
        n =len(nums)
        while(r<n):
            for i in range (l,r+1):
                maxx=max(nums[i],maxx)
            result.append(maxx)
            maxx=float('-inf')
            l+=1
            r+=1
        return result
        