class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int profit=0,minn=prices[0],maxx=prices[0];
        int current_profit=0;
        for(int i=1;i<prices.size();i++)
        {
         minn= std::min(prices[i],minn);   
         profit =std:: max(profit,prices[i]-minn);
        }
        return profit;
        
    }
};
