class Solution {
public:
    int diameterOfBinaryTree(TreeNode* root) {
        int diameter = 0;
        calculateHeight(root, diameter);
        return diameter;
    }
    
private:
    int calculateHeight(TreeNode* node, int& diameter) {
        if (node == nullptr) {
            return 0;
        }
        
        int leftHeight = calculateHeight(node->left, diameter);
        int rightHeight = calculateHeight(node->right, diameter);
        
        // Update the diameter at this node
        diameter = std::max(diameter, leftHeight + rightHeight);
        
        // Return the height of the current node
        return std::max(leftHeight, rightHeight) + 1;
    }
};
