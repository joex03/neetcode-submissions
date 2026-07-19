class Solution {
public:
    vector<int> dailyTemperatures(vector<int>& temperatures) 
    {
        
         int n = temperatures.size();
    std::vector<int> result(n, 0);
    
    for (int i = n - 2; i >= 0; --i) {
        int j = i + 1;
        while (j < n && temperatures[i] >= temperatures[j]) {
            if (result[j] == 0) break; // No warmer day found after j
            j += result[j]; // Jump to the next day where a warmer temperature was found
        }
        if (temperatures[i] < temperatures[j]) {
            result[i] = j - i;
        }
    }
    
    return result;
    }

};
