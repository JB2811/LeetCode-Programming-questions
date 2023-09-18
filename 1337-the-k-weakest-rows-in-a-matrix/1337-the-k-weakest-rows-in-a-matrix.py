class Solution:
    def kWeakestRows(self, l: List[List[int]], k: int) -> List[int]:
        a=[]; s=[]
        n=len(l)
        for r in l:
         if(r.count(0)>0):
          t=(r.index(0))
         else:
          t=len(r)
         a.append(t)
        print(a)
        while(n>0):
         t=a.index(min(a))
         s.append(t)
         a[t]=10000000
         n=n-1
        print(s)
        return s[:k];
        