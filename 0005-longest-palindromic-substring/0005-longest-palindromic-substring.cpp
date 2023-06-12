class Solution 
{ public:
  int p[1000][1000],g;
  int checkpalindrome(string s)
    { int i,l;
      int n=s.length();
      l=0;
      for(i=0;i<n/2;i++)
      { if(s[i]==s[n-i-1])
        { l++;}}
      if(l==n/2)
      { return 1;}
      else
      { return 0;}}
    int longestPalindromeSubStr(string &s,int z,int x)
    { int n=s.length();
      int i,j,r,q;
      r=1;
      for(i=x-1;i>=z;i--)
      { q=0;
        for(j=i+1;j<=x;j++)
        { if(s[i]==s[j] && p[i][j]==0)
          { if(checkpalindrome(s.substr(i,j-i+1)))
            { q=p[i+1][j-1];
              if(i!=j)
              { q=q+2;}
              if(r<=q)
              {r=q;
               g=i;}}
              p[i][j]=q;}
          if(((j-i+1)>=r) && (j>=(g+r-1)))
          { p[i][j]=r;}
          else
          { p[i][j]=max(p[i][j],p[i][j-1]);}}}
      return p[z][x];}
    string longestPalindrome(string &s)
    { int n=s.length();
      if(checkpalindrome(s))
      { return s;}
      else
      { for(int i=0;i<n;i++)
        { p[i][i]=1;}
        int l=longestPalindromeSubStr(s,0,n-1);
        string q=s.substr(g,l);
        return q;}}};