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
    int add(ListNode* &l1,ListNode* &l2)
    { int c=0;
      if(l1->next!=NULL && l2->next!=NULL)
      { c=add(l1->next,l2->next);}
      
      l1->val=(l2->val)+(l1->val)+c;
      if(l1->val>9)
      { int t=(l1->val)/10;
        l1->val=l1->val%10;
        return t;}
      return 0;}
 
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) 
    { 
      ListNode *r1,*r2,*t;
      r1=new ListNode();
      r1=l1;
      r2=new ListNode();
      r2=l2;
      
      while(l1->next!=NULL || l2->next!=NULL)  
      { if(l1->next!=NULL && l2->next!=NULL)
        { l1=l1->next;
          l2=l2->next;}
        else if(l1->next!=NULL && l2->next==NULL)
        { t=new ListNode();
          t->val=0;
          t->next=r2;
          r2=t;
          l1=l1->next;}
        else if(l1->next==NULL && l2->next!=NULL)
        { t=new ListNode();
          t->next=r1;
          t->val=0;
          r1=t;
          l2=l2->next;}}  
      
      int c=add(r1,r2);
      if(c>0)
      { t=new ListNode();
        t->val=c;
        t->next=r1;
        r1=t;}

      return r1;}};
