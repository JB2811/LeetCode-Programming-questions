/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution 
{ public:
    vector<int> a;
    TreeNode* decoy;
    int t;
 
    void findnode(TreeNode* n,int d,int k)
    { if(n!=NULL && d<k)
      { findnode(n->left,d+1,k);
        findnode(n->right,d+1,k);}
      if(n!=NULL && d==k)
      { a.push_back(n->val);}}
    
    void findparent(TreeNode* n)
    {if(n!=NULL && decoy!=n)
     {if(n->left!=NULL && n->left->val==decoy->val)
      { t=decoy->val;
        decoy=n;}
      else if(n->right!=NULL && n->right->val==decoy->val)
      { t=decoy->val;
        decoy=n;}
      else
      { findparent(n->left);
        findparent(n->right);}}}
    
    vector<int> distanceK(TreeNode* root, TreeNode* target, int k) 
    { decoy=target;
      findnode(decoy,0,k);
      k--;
      t=decoy->val;
      while(k>=0 && decoy!=root)
      { findparent(root);
        if(decoy->left!=NULL && decoy->left->val==t)
        { findnode(decoy->right,1,k);}
        else
        { findnode(decoy->left,1,k);}
          k--;}
      if(decoy!=root && decoy!=target)
      { a.push_back(decoy->val);}   
      else if(k<0 && decoy==root)
      { a.push_back(decoy->val);}
      return a;}};