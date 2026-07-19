class Solution {
public:
    int singleNumber(vector<int>& nums) 
    {
     unordered_map<int,int> counter;
     for(auto&k:nums)
     {
        counter[k]++;
     }
     for(auto&k:counter){
        if(k.second!=2)
        {
            return k.first;
        }
     }   
    }
};
