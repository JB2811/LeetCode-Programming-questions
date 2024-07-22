/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode reverseKGroup(ListNode head, int k) 
    { ListNode l=new ListNode();
      ListNode f=l;
      ListNode y=head;
      while(y!=null)
      { int j=k;
        while(j>0)
        { int i=1;
          ListNode t=y;
          while(i<j && t!=null)
          { t=t.next;
            i++;}
          if(t==null)
          { break;}
          ListNode x=new ListNode();
          x.val=t.val;
          l.next=x;
          l=l.next;
          j--;}
       if(j>0)
       { while(y!=null)
         { ListNode x=new ListNode();
           x.val=y.val;
           l.next=x;
           l=l.next;
           y=y.next;}}
       else
       { int i=0;
         while(i<k)
         { y=y.next;
           i++;}}}
     return f.next;
        
    }
}