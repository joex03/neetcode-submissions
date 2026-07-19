class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxx=0
        l=0
        r=len(heights)-1
        while l<r:
            h=min(heights[l],heights[r])
            w=r-l
            area=h*w
            maxx=max(maxx,area)
            if h==heights[l]:
                l+=1
            elif h==heights[r]:
                r-=1
        return maxx