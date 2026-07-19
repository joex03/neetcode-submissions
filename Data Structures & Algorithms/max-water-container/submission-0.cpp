class Solution {
public:
    int maxArea(std::vector<int>& heights) {
        int result = 0;
        int lefti = 0;
        int righti = heights.size() - 1;
        
        while (lefti < righti) {
            
            int current_area = (righti - lefti) * std::min(heights[lefti], heights[righti]);
            
            result = std::max(result, current_area);

            
            if (heights[lefti] < heights[righti]) {
                lefti++;
            } else {
                righti--;
            }
        }
        
        return result;
    }
};
