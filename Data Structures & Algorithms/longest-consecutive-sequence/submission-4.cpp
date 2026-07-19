class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        if(nums.size()==0){
            return{};
        }
        
      
        vector<int>count;
        std::sort(nums.begin(),nums.end());
        int current_counter=1;
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i]==nums[i-1])
            {
                continue;
            }
            if(nums[i]==(nums[i-1]+1))
            {
                current_counter++;
            }
            else
            {
                count.push_back(current_counter);
                current_counter=1;
            }
        }
        count.push_back(current_counter);
        int max_value = *std::max_element(count.begin(), count.end());  
        return max_value; 
    }
};
