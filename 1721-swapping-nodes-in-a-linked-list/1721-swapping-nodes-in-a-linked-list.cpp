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
    ListNode* swapNodes(ListNode* head, int k) 
    { ListNode *temp1,*temp;
      temp=head;
      int i=1;
      while(temp!=NULL && i<k)
      { temp=temp->next;
        i++;}
      temp1=temp;
      cout<<(temp1->val);
      int l=k;
      while(temp!=NULL)
      { temp=temp->next;
        l++;}
      k=l-k;
      temp=head;
      i=1;
      while(temp!=NULL && i<k)
      { temp=temp->next;
        i++;}
      int t=temp1->val;
      temp1->val=temp->val;
      temp->val=t;
      return head;
    }
};