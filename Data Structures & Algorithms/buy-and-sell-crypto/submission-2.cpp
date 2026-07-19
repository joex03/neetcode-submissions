class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int minn=prices[0],profit=0;
        for(int i=1;i<prices.size();i++)
        {
            minn=std::min(minn,prices[i]);
            profit=std::max(profit,prices[i]-minn);
        }
        return profit;
    }
};
