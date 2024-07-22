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
    public ListNode mergeKLists(ListNode[] lists) {
        int n=lists.length;
        
        ListNode l=new ListNode();;

        
        for(int i=0;i<n;i++)
        { ListNode t=lists[i];
          
          while(t!=null)
          { ListNode x=l;
            //System.out.println(t.val+" "+x.val);
            while(x!=null && x.next!=null)
            { if(t.val<x.next.val)
              { break;}
              x=x.next;}
            if(x==null)
            { x.val=t.val;}
            else
            { ListNode y=new ListNode();
              y.val=t.val;
              y.next=x.next;
              x.next=y;}
            t=t.next;}}
        
        return l.next;
        
    }
}