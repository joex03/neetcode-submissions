class Solution {
public:
    int findDuplicate(vector<int>& nums) {
        unordered_map<int,int> counter;
        for(auto &k:nums){
            counter[k]++;
            if(counter[k]>1){
                return k;
            }
        }
    }
};
