class Solution {
public:
    int longestConsecutive(vector<int>& nums) 
    {
        if(nums.size()==0){
            return 0;
        }
        int maxx=1;
        int current_max=1;
        std::sort(nums.begin(),nums.end());
        for(int i=1;i<nums.size();i++)
        {
            if(nums[i-1]==(nums[i]-1))
            {
                current_max++;
            }
            else if(nums[i-1]==(nums[i]))
            {
                continue;
            }
            else
            {
                current_max=1;
            }
        maxx=std::max(maxx,current_max);
        }
        return maxx;
    }
};
