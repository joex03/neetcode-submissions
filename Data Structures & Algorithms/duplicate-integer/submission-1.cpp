class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
        int size=nums.size();
        for(int i=0;i<size;i++)
        {
            for(int j=i;j<size;j++)
            {
                if(nums[i]==nums[j] && i!=j)
                {
                    return true;
                }
            }
        }
        return false;
    }
};
