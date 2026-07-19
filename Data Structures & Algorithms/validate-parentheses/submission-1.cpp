class Solution {
public:
    bool isValid(string s) 
    {
        std::stack<char> opened;
        unordered_map<char,char> listt={{')','('},{'}','{',},{']','['}};
        for (char c : s) {
            if (listt.count(c)) { // If c is a closing bracket
                if (opened.empty() || opened.top() != listt[c]) {
                    return false; // Mismatch or stack is empty
                }
                opened.pop(); // Pop the matched opening bracket
            } else {
                opened.push(c); // Push opening brackets onto the stack
            }
        }

        return opened.empty(); // True if all brackets are matched, otherwise false

    }
};
