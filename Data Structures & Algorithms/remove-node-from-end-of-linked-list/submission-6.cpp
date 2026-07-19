/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */

class Solution {
public:
     ListNode* removeNthFromEnd(ListNode* head, int n) {
        vector<int> arr;
        ListNode * temp=head;
        while(temp){
            arr.push_back(temp->val);
            temp=temp->next;
        }
        int size=arr.size();
        int targetindexfromstart=size-n;
        if(targetindexfromstart==0){
            head=head->next;
            return head;
        }
        int counter=0;
        ListNode * curr=head;
        ListNode * prev=nullptr;
        while(curr){
            if(counter == targetindexfromstart){
                prev->next=curr->next;
                return head;
            }
            else{
                counter++;
                prev=curr;
                curr=curr->next;
            }
        }
        return head;
     }
};