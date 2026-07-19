class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        nums.sort()
        size=len(nums)
        return nums[size-k]