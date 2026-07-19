class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) 
    {
     vector<int> result(temperatures.size(),0);
     stack<int >temp;
     for(int i=0;i<temperatures.size();i++)
     {
        while(!temp.empty() && temperatures[temp.top()] < temperatures[i] )
        {
            
            result[temp.top()] = i - temp.top();
            temp.pop();
        }
        temp.push(i);
     }   
     return result;
    }

};
