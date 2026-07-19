class Solution 
{
public:
    vector<int> productExceptSelf(vector<int>& nums) 
    {
        vector<int> result;
        int temp=1;
        for(int i=0;i<nums.size();i++)
        {
            int tempp=nums[0];
            nums.erase(nums.begin());
            for(auto& K:nums)
            {
                temp*=K;
            }
            
            result.push_back(temp);
            nums.push_back(tempp);
            temp=1;
        }
        return result;
    }
};
