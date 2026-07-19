class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        vector<int> result;
        int temp=1;
        for(int i=0;i<nums.size();i++)
        {
            int tempp=nums[0];
            nums.erase(nums.begin());
            for(auto& k:nums)
            {
                temp*=k;
            }
            result.push_back(temp);
            temp=1;
            nums.push_back(tempp);

        }
        return result;
    }
};
