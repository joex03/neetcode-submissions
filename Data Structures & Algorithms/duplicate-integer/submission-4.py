class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mapp=Counter(nums)
        for num in nums:
            if mapp[num]>1:
                return True
        return False