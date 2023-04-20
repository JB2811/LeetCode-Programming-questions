/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution 
{ public:
   int pathleft(TreeNode* root,int i)
   { int n1,n2;
     if(root==NULL)
     { return i;}
     n1=pathright(root->right,i+1);
     n2=findpath(root->left,1,0);
     return n1>n2?n1:n2;}
   int pathright(TreeNode* root,int j)
   { int n1,n2;
     if(root==NULL)
     { return j;}
     n1=pathleft(root->left,j+1);
     n2=findpath(root->right,0,1);
     return n1>n2?n1:n2;}
   int findpath(TreeNode* root,int i,int j)
   { if(root!=NULL)
     { i=pathright(root->right,i);
       j=pathleft(root->left,j);
       return i<j?j:i;}
     return 0;}
   int longestZigZag(TreeNode* root) 
   { return findpath(root,0,0);}};