class Solution {
public:
    int characterReplacement(string s, int k) 
    {
     int left=0,right=0;
     int maxx=0,result=0;
     vector<int> counter(26,0);
     for(int right=0;right<s.size();right++)
     {
        counter[s[right]-'A']++;
         maxx = std::max(maxx, counter[s[right] - 'A']);
        while(right-left+1-maxx > k)
        {
            counter[s[left]-'A']--;
            left++;   
        }
        result=std::max(result,right-left+1);

     }       
     return result;
    }
};
