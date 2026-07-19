class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        row=len(triplets) #each col is of size=3 
        result=[]
        maxx=0
        maxy=0
        maxz=0
        for t in triplets:
            # we need to make sure that target[0] is max of t[0]
            if t[0]<=target[0] and t[1]<=target[1] and t[2]<=target[2]:
                maxx=max(maxx,t[0])
                maxy=max(maxy,t[1])
                maxz=max(maxz,t[2])
        result.append(maxx)
        result.append(maxy)
        result.append(maxz)
        return result==target
