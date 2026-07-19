#include<stack>
class Solution {
public:
    bool isValid(string s) 
    {
        std::stack<char>st; // to place the opening parenthese
        std::unordered_map<char,char> valid={{')','('},{'}','{'},{']','['}};
        for(auto &k:s)
        {
            if(valid.count(k)) // then this is a key closing one
            {
                char temp=st.empty()?'#':st.top();
                if(st.empty()|| temp!=valid[k])
                {
                    return false;
                }
                st.pop();
            }
            else  //we will enter here if this is opening
            {
                st.push(k);
            }
        }
        return st.empty();
    }
};
