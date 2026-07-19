class Solution:
    def checkValidString(self, s: str) -> bool:
        lowOpen=0
        highOpen=0
        for c in s: # the concept here means 
            if c=='(':
                lowOpen+=1
                highOpen+=1
            elif c==')':
                lowOpen-=1
                highOpen-=1
            else:
                lowOpen-=1
                highOpen+=1

            if lowOpen<0:
                lowOpen=0
            if highOpen<0: # ')' only 
                return False
        return lowOpen==0