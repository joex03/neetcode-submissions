
class Solution {
public:
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        std::vector<int> arr;
        ListNode* temp = head;

        // Populate the vector with values from the linked list
        while (temp != nullptr) {
            arr.push_back(temp->val);
            temp = temp->next;  // Move to next node
        }

        int size = arr.size();
        int targetIndex = size - n;  // Calculate the index of the node to remove

        // Edge case: If we're removing the head
        if (targetIndex == 0) {
            ListNode* newHead = head->next;
            delete head;  // Free the old head
            return newHead;
        }

        // Traverse again to remove the node
        ListNode* prev = nullptr;
        ListNode* curr = head;
        int counter = 0;

        while (curr) {
            if (counter == targetIndex) {
                prev->next = curr->next;  // Remove the target node
                delete curr;  // Free memory of the deleted node
                return head;
            }
            prev = curr;
            curr = curr->next;
            counter++;
        }
        
        return head;  // In case n is invalid, return the original list (though this shouldn't happen)
    }
};
