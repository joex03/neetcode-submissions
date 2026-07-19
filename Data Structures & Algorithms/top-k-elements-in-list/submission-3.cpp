class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) 
    {
        std::unordered_map<int,int> count;//k first is the num second is the feq
        for(auto& num:nums)  // we have counted the rep of each no.
        {
            count[num]++;
        }
        vector<vector<int>> bucket(nums.size()+1);
        for(auto& k: count)
        {
            bucket[k.second].push_back(k.first);
        }
        vector<int>result;
        for(int i=nums.size();i>0 && result.size()<k ;i--)
        {
            for(auto& s:bucket[i])
            {
                result.push_back(s);
                if(result.size()==k)
                {
                    return result;
                   
                }
            }

        }
        return result;
        
    }
};
