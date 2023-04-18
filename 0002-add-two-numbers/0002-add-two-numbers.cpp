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
class Solution 
{ public:
   ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
   { ListNode *l3,*temp,*head;
     l3=new ListNode();
     head=new ListNode();
     temp=new ListNode();
     temp=NULL;
     while(l1!=NULL || l2!=NULL)
     { l3=new ListNode();
       if(l1==NULL)
       { l1=new ListNode();}
       else if(l2==NULL)
       { l2=new ListNode();} 
       l3->val=l1->val+l2->val;
       if(l3->val>9)
       { l3->val%=10;
         if(l2->next==NULL)
         { l2->next=new ListNode();}
         l2->next->val++;}
       if(temp!=NULL)
       { temp->next=l3;}
       else
       { head=l3;}
       temp=l3;
       l2=l2->next;
       l1=l1->next;}
     return head;}};