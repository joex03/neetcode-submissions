class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
     int result=0;
     unordered_map<int,int> counter;
     for(auto &k:nums)
     {
        counter[k]++; // first one is the number itself the second is the counter
     }
     for(auto &k:counter) {
        if(k.second!=2){
            return k.first;
        }
     } 
    }
};
