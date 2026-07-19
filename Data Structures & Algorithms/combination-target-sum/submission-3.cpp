class Solution {
public:
    vector<vector<int>> combinationSum(vector<int>& nums, int target) {
        vector<vector<int>> result;
        vector<int> set;
        int level=0;
        Back_tracking(level, set, target, nums, result);
        return result;
    }
    void Back_tracking(int level, vector<int> &set, int target, vector<int>& nums, vector<vector<int>> &result){
        if(level == nums.size() ||target < 0 ){
            return;
        }
        if(target == 0){
            result.push_back(set);
            return;
        }
        set.push_back(nums[level]);
        Back_tracking(level,set,target-nums[level],nums,result);
        set.pop_back();
        Back_tracking(level+1,set,target,nums,result);

    }
};
