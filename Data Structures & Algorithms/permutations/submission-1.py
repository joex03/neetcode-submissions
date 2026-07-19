class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==0:
            return [[]]
         # i need to take the number and insert in all possible places nums[0]
        perms=self.permute(nums[1:])
        result=[]
        for p in perms:
            for i in range (len(p)+1):
                temp=p.copy()
                temp.insert(i,nums[0])
                result.append(temp)
        return result

