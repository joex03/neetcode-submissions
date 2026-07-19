class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        std::unordered_map<string,vector<string>> anagram;
        for(auto & s:strs)
        {
            string copy=s;
            std::sort(s.begin(),s.end());
            anagram[s].push_back(copy);
        }
        vector<vector<string>> result;
        for(auto& k:anagram)
        {
            result.push_back(k.second);
        }
        return result;
    }
};
