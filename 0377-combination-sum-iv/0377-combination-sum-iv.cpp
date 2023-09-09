class Solution 
{ public:
    int combinationSum4(vector<int>& nums, int target) 
    { int j,i,s;
      unsigned long int d[target+1];
      for(i=1;i<=target;i++)
      { d[i]=0;}
      s=0;
      for(j=1;j<=target;j++)
      { for(i=0;i<nums.size();i++)
        { if(nums[i]<j)
          { d[j]=d[j]+d[j-nums[i]];}
          else if(nums[i]==j)
          { d[j]++;}}}
      return d[target];}};