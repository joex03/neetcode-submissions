class Solution {

public:
    vector<string> generateParenthesis(int n) 
    {
    vector<string>result;
    string str="";
    int open=0,close=0;
    backtrack(result,str,open,close,n);
     return result; 
    }


void backtrack(vector<string> &result,string str,int open,int close,int n)
     {
        if(str.size()==n*2)
        {
            result.push_back(str);
            return;
        }
        if(open<n)
        {
            backtrack(result,str +"(", open +1, close, n);  
        }
        if(close<open)
        {
            backtrack(result,str +")", open, close +1, n);
        }
        
     }  


};
