class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx=0
        l=0
        r=len(heights)-1
        while l<=r:
            height=min(heights[l],heights[r])
            width=r-l
            area=height*width
            maxx=max(maxx,area)
            if heights[l]<heights[r]:
                l+=1
            elif heights[r]<heights[l]:
                r-=1
            else:
                l+=1
                r-=1
        return maxx
#[1,7,2,5,4,7,3,6]
#[0,1,2,3,4,5,6,7]
#[l=1,]