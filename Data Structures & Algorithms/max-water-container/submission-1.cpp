class Solution {
public:
    int maxArea(std::vector<int>& heights) 
    {
        int result=0,current_area=0;
        int left=0,right=heights.size()-1;
        while(left<right)
        {
            current_area=std::min(heights[left],heights[right])*(right-left);
            result=std::max(result,current_area);
            if(heights[left]<heights[right])
            {
                left++;
            }
            else
            {
                right--;
            }
        }
        return result;
    }
};
