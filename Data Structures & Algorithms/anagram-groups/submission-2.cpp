class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
       unordered_map<string,vector<string>> anagram;
       for(auto&k:strs)
       {
            string temp=k;
            std::sort(k.begin(),k.end());
            anagram[k].push_back(temp);
       }
       vector<vector<string>> result;
       for(auto&k:anagram)
       {
        result.push_back(k.second);
       }
       return result;
    }
};
