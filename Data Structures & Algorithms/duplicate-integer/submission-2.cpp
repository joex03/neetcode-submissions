class Solution {
public:
    bool hasDuplicate(vector<int>& nums) 
    {
       unordered_map<int,int> seen;
       for(int i=0;i<nums.size();i++)
       {
        if(seen.find(nums[i])!=seen.end())  //if we find it 
        {
            return true;
        }
        else
        {
            seen[nums[i]]=i;
        }
       }
       return false;
    }
};
