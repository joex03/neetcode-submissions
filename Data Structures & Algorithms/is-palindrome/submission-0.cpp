class Solution {
public:
    bool isPalindrome(string s) 
    {
        int right=s.size()-1;
        int left=0;
        while(left<right)
        {
            
            while(left<right && !std::isalnum(s[left]))
            {
                left++;
            }
            while(left<right && !std::isalnum(s[right]))
            {
                right--;
            }
            if(std::tolower(s[left])!=std::tolower(s[right]))
            {
                return false;
            }
            left++;
            right--;
        }
        return true;
    }
};
