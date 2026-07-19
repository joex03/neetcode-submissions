class Solution {
public:
    int minEatingSpeed(vector<int>& piles, int h) 
    {
        int left=1,count=0;
        int right =*max_element(piles.begin(),piles.end());
        if(piles.size()==h){
            return right;
        }
        int mid =left+(right-left)/2;
        while(left<=right){
             mid =left+(right-left)/2;
             count =0;
            for(int i=0;i<piles.size();i++){
                int temp =(piles[i] + mid - 1) / mid; // the complete time taken to eat all the banans
                count+=temp;
            }
            if(count<=h){ // this means we finished eating in less than the time required so valid
                right = mid-1;
            }
            else{ // this means we didn't finish in the required time
                left=mid+1;
            }
        }
     return left;   
    }
};
