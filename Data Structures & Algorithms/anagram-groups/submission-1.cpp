class Solution {
public:
    vector<vector<string>> groupAnagrams(vector<string>& strs) 
    {
        vector<vector<string>> result;
        unordered_map<string,vector<string>> comp;
        for(auto& k:strs)
        {
            string temp=k;
            std::sort(k.begin(),k.end());
            comp[k].push_back(temp);
        }
        for(auto& k:comp)
        {
            result.push_back(k.second);
        }
        return result;
    }
};
