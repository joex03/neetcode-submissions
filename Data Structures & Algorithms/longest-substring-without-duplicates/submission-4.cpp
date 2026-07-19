#include<string>
#include<vector>
class Solution {
public:
    int lengthOfLongestSubstring(string s) 
    {
        if(s.size()==1){
            return 1;
        }
     int maxx=0;
     std::unordered_set<char>set;
     set.insert(s[0]);
     int left=0;
     for(int i=1;i<s.size();i++)
     {     
        while(set.find(s[i])!=set.end())
        {
            set.erase(s[left]);
            left++;
        }
     
        set.insert(s[i]);
        maxx=std::max(maxx,i-left+1);
    }
        return maxx;
    }
    
};
