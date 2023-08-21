class Solution 
{ public:
    bool repeatedSubstringPattern(string s) 
    { int n=s.length();
      int i,j,k;
      if(n==1)
      { return false;}
      for(j=n/2;j>0;j--)
      { if(n%j==0)
        { int l=j;
          cout<<l;
          for(i=0;i<(n/j);i++)
          { for(k=0;k<j;k++)
            { if(s[k]==s[l+k])
              { continue;}
              else
              { break;}}
            if(k<j)
            { break;}
            l=l+j;
            if(l>=n)
            { l=l-j; }}
          if(i==(n/j))
          { return true;}}}
      return false; }};