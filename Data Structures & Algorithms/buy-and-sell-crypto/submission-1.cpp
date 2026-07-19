class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int profit=0;
        int minn=prices[0];
        for(int i=1;i<prices.size();i++)
        {
            minn=std::min(prices[i],minn);
            profit=std::max(prices[i]-minn,profit);
        }
        return profit;
    }
};
