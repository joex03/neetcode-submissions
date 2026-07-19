class Solution {
public:
    vector<vector<int>> subsets(vector<int>& nums) {
        int level=0;
        vector<vector<int>> result;
        vector<int> subsets;
        Back_tracking(nums,level,result,subsets);
        return result;

    }
    void Back_tracking(vector<int> nums, int level, vector<vector<int>> &result, vector<int> &subsets){
        if(level==nums.size()){
            result.push_back(subsets);
            return;
        }
        subsets.push_back(nums[level]);
        Back_tracking(nums,level+1,result,subsets);
        subsets.pop_back();
        Back_tracking(nums,level+1,result,subsets);

    }
};
