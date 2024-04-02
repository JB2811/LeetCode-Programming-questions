class Solution(object):
 def isIsomorphic(self, s, t):
  l=[]; l2=[]
  sn=0; tn=0
  for i in range(len(s)):  
   if(s[i] not in l):
    l.append(s[i])
   sn=sn*10+l.index(s[i])
   if(t[i] not in l2):
    l2.append(t[i])
   tn=tn*10+l2.index(t[i])
  if(sn==tn):
   return True
  else:
   return False 
   