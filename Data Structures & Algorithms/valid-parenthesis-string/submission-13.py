class Solution:
    def checkValidString(self, s: str) -> bool: # count the unmatched
        minOpen=0
        maxOpen=0
        for c in s:
            if c=='(':
                minOpen+=1
                maxOpen+=1
            elif c==')':
                minOpen-=1
                maxOpen-=1
            else: # c here is *
                minOpen-=1
                maxOpen+=1
            if minOpen<0: # ( can't be negative its always 0 or bigger
                minOpen=0
            if maxOpen<0:# this mean we only have closed brace case:() max here is zero and true
                return False         
        return minOpen==0      


            
            