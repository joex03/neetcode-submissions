#include<stack>
class Solution {
public:
    bool isValid(string s) 
    {
    
        unordered_map<char,char> matchy={{')','('},{']','['},{'}','{'}};
        stack<char> open;
        for(auto &k:s)
        {
            if(matchy.count(k)==1)   // this means k is closing
            {
                char temp=open.empty()?'#':open.top();
                if(matchy[k]!=temp||open.empty())
                {
                    return false;
                }
                open.pop();
            }
            else // k is opening
            {
                open.push(k);
            }
        }
        return open.empty();
    }
};
