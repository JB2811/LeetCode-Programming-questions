class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
     l=[]
     for x in strs:
      l.append(len(x))
     x=l.index(min(l))
     s=min(l)
     x=strs[x]
     print(x," ",s)
     for i in range(0,len(x)):
      for j in range(0,len(strs)):
       if(x[:(len(x)-i)] not in strs[j][:s]):
        s=s-1
        break
      if(j==len(strs)):
       return x[:s]
     return x[:s]
        