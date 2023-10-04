import copy
class Solution:
    l=[[" "],[],['a','b','c'],['d','e','f'],['g','h','i'],['j','k','l'],['m','n','o'],['p','q','r','s'],['t','u','v'],['w','x','y','z']]
    def letterCombinations(self, digits: str) -> List[str]:
     d=list(digits)
     for i in range(len(d)):
      d[i]=int(d[i])
     if(len(d)>0):
      a=self.l[d[0]]
     else:
      a=[]
      return a 
     for i in range(1,len(d)):
      s=[]
      for j in range(len(a)):
       for k in self.l[d[i]]:
        s.append(a[j]+k)
      a=copy.deepcopy(s);
      s=[]
     return a
      