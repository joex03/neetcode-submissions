class Solution {
public:
    int maxProfit(vector<int>& prices) 
    {
        int left=prices[0];
        int profit=0;
        for(int i=0;i<prices.size();i++){
         if(prices[i]<left){
            left=prices[i];
         }   
            profit=max(profit,prices[i]-left);
        }
        return profit;
    }
};
