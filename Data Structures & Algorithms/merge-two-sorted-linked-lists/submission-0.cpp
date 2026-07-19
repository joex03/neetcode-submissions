class Solution {
public:
    ListNode* mergeTwoLists(ListNode* list1, ListNode* list2) {
        // Create a dummy node to simplify the merge process
        ListNode dummy(0);
        ListNode* tail = &dummy; // Pointer to form the merged list

        // Traverse both lists and append the smaller node to the merged list
        while (list1 && list2) {
            if (list1->val < list2->val) {
                tail->next = list1;
                list1 = list1->next;
            } else {
                tail->next = list2;
                list2 = list2->next;
            }
            tail = tail->next;
        }

        // If either list has remaining elements, append them
        if (list1) {
            tail->next = list1;
        } else {
            tail->next = list2;
        }

        // Return the merged list (skip the dummy node)
        return dummy.next;
    }
};
