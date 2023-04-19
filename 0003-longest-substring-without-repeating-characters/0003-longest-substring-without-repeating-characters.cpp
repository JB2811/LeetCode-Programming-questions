class Solution 
{ public:
    int lengthOfLongestSubstring(string s)
    { int i,t,j,c,l=0,n=s.length();
      string r;
      for(i=0;i<n;i++)
      { c=1;
        r="";
        for(j=i+1;j<n;j++)
        { if(s[i]!=s[j])
          { t=r.find_first_of(s[j]);
            if(t>=0)
            { j=n;
              continue;}
            c++;
            r=r+s[j];}
          else
          { j=n;}}
        if(l<c)
        { l=c;}}
      return l;}};