import copy
class Solution:
    def convert(self, s: str, n: int) -> str:
     s=list(s)
     l=copy.deepcopy(s)
     d=[]
     i=0
     for i in range(n):
      d.append(0)
      d[i]=[]
     print(len(d))
     i=0
     k=0
     while(i<len(s)):
      if(k<n):
       d[k].append(s[i])
       k+=1
       i+=1
      else:
       k-=2
       if(k<0):
        k=0
       while(k>=0 and i<len(s)):
        d[k].append(s[i])
        i+=1
        k-=1
       k+=2
     a=""
     for i in range(n):
      a=a+"".join(d[i])
     return a 