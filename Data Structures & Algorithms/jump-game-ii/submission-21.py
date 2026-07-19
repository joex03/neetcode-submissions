class Solution:
    def jump(self, nums: List[int]) -> int:
        # el concept hna nmshy [2,1,3,5] nmshy kol steps nums[0]
        #3shan n2ked enna shofna 1,3 shofna khalas?
        #counter++ ba2a we
        counter=0
        end=nums[0]
        maxJump=end
        size=len(nums)
        if size==1:
            return 0
        for i in range(1,size-1):
            maxJump=max(maxJump,nums[i]+i)
            if end==i:
                counter+=1
                end=maxJump
        counter+=1
        return counter