class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapper={}
        l=0
        r=0
        for r in range(len(nums)):
            if nums[r] in mapper:
                mapper[nums[r]]+=1
                return True
            else:
                mapper[nums[r]]=1
            if (r-l+1)>k:
                mapper[nums[l]]-=1
                if mapper[nums[l]]==0:
                    del mapper[nums[l]]
                l+=1

        return False