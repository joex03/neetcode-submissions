class Solution {
public:
    int search(vector<int>& nums, int target) 
    {
        int left = 0, right = nums.size() - 1;
        while (left <= right)
        {
            int mid = left + (right - left) / 2;  // Calculate the mid point

            if (nums[mid] == target)  // Target found
            {
                return mid;
            }
            else if (nums[mid] < target)  // Target is in the right half
            {
                left = mid + 1;  // Move the left boundary to mid + 1
            }
            else  // Target is in the left half
            {
                right = mid - 1;  // Move the right boundary to mid - 1
            }
        }
        return -1;  // Target not found
    }
};
