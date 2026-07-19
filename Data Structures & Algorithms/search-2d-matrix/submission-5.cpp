class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
         if (matrix.empty() || matrix[0].empty()) {
            return false;
        }
        int rows= matrix.size();
        int col = matrix[0].size();
        int left=0;
        int right = rows*col-1;
        while(left<=right){
            int mid = left+(right-left)/2;
            int midvalue= matrix[mid/col][mid%col];
            if(midvalue == target){
                return true;
            }
            else if (midvalue < target ){
                left =mid+1;
            }
            else if (midvalue > target){
                right= mid -1;
            }
        }
        return false;
    }

};
