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
        vector<int>arr;
        ListNode* temp=head;
        while(temp){
            arr.push_back(temp->val);
            temp=temp->next;
        }
        int size = arr.size();
        int targetindex=size-n;
        int targetvalue=arr[targetindex];

        if(targetindex == 0){
            head=head->next;
            return head;
        }

     ListNode* prev=nullptr;
     ListNode* curr=head;
    int counter=0;
     while(curr){
        if (counter == targetindex){
            prev->next=curr->next;
            return head;
        }
        else {
            prev=curr;
            curr=curr->next;
            counter++;
        }
     } 
     return head;
    }
};