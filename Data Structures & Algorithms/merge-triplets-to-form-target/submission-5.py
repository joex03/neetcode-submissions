class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        rowSize=len(triplets)
        maxx,maxy,maxz,=0,0,0
        for temp in triplets:
            if (temp[0]>target[0] or temp[1]>target[1] or temp[2]>target[2]):
                continue
            else:
                maxx=max(maxx,temp[0])
                maxy=max(maxy,temp[1])
                maxz=max(maxz,temp[2])
        result=[]
        result.append(maxx)
        result.append(maxy)
        result.append(maxz)
        return result==target

