/** QUESTION
 * You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
 *
 * You may assume the two numbers do not contain any leading zero, except the number 0 itself.
 *
 * Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
 * Output: 7 -> 0 -> 8
 */

/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        int sum;

        ListNode* l = new ListNode(0);
        ListNode* r = l;

        do{
            sum = (l1 == NULL ? 0 : l1->val) + (l2 == NULL ? 0 : l2->val) + (l->next == NULL ? 0 : l->next->val);
            
            if (sum >= 10){
                sum = sum % 10;
                l->next = new ListNode(sum);
                l->next->next = new ListNode(1);
            } else
                l->next = new ListNode(sum);
                
            l = l->next;
            l1 = (l1 == NULL ? NULL : l1->next);
            l2 = (l2 == NULL ? NULL : l2->next);
        }while(l1 != NULL || l2 != NULL);
        
        return r->next;
    }
};
