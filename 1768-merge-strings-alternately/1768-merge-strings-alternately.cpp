class Solution 
{ public:
    string mergeAlternately(string word1, string word2) 
    { int i,j,n;
      string r;
      n=(word1.length()<word2.length())?word1.length():word2.length();
      for(i=0;i<n;i++)
      { r=r+word1[i]+word2[i];}
      if(i>=word1.length())
      { while(i<word2.length())
        { r=r+word2[i];
          i++;}}
      else
      { while(i<word1.length())
        { r=r+word1[i];
          i++;}}
      return r;}};