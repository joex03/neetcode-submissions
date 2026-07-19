class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) 
    {
       unordered_map<int,int> complement;
       for(int i=0;i<numbers.size();i++)
       {
        int comp=target-numbers[i];
        if(complement.find(comp)!=complement.end()) // if we find it 
        {
            return {complement[comp]+1,i+1};
        }
        complement[numbers[i]]=i;
       }
       return {};
    }
};
