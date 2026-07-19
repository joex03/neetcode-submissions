class Solution {
public:
    vector<int> twoSum(vector<int>& numbers, int target) 
    {
        int left=0;
        int right=numbers.size()-1;
         int temp=numbers[left]+numbers[right];
        while(left<right)
        {
            if(temp==target){
                return{left+1,right+1};
            } 
            if(temp>target)
            {
                right--;
                
            }
            if(temp<target)
            {
                left++;
            }
           
             temp=numbers[left]+numbers[right];
        }
        return {};
        
    }
};
