class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res=[]
        for i in range(len(nums)):
            if i>0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1,len(nums)):
                if j>i+1 and nums[j]==nums[j-1]:
                    continue
                l,h=j+1,len(nums)-1
                while l<h:
                    summ=nums[i]+nums[l]+nums[h]+nums[j]
                    if summ==target:
                        res.append([nums[i],nums[j],nums[l],nums[h]])
                        # we found answer but we need to avoid dups
                        l+=1
                        h-=1
                        while l<h and nums[l]==nums[l-1]:
                            l+=1
                        while l<h and h+1<len(nums) and nums[h]==nums[h+1]:
                            h+=1
                    elif summ<target:
                        l+=1
                    elif summ>target:
                        h-=1
        return res
                