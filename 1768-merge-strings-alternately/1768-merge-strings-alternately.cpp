class Solution 
{ public:
    string mergeAlternately(string word1, string word2) 
    { int i,j,n1,n2;
      string r;
      n1=word1.length();
      n2=word2.length();
      i=0;
      while(i<n1 && i<n2)
      { r=r+word1[i]+word2[i];
        i++;}
      if(i>=n1)
      { while(i<n2)
        { r=r+word2[i];
          i++;}}
      else
      { while(i<n1)
        { r=r+word1[i];
          i++;}}
      return r;}};