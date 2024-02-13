class Solution:
 def minOperations(self, s: str) -> int:
  l=[]
  i=0
  v=0
  while(i<len(s)):
   l.append(s[i:i+2])
   i+=2
  x=""
  if(l.count('01')>l.count('10')):
   x='01'
  elif(l.count('01')<l.count('10')):
   x='10'
  if(x==""):
   if(s[0]=='0'):
    x='01'
   else:
    x='10'
  o=0
  if(len(s)%2!=0):
   if(x=='01' and l[len(l)-1]!='0'):
    o+=1
   elif(x=='10' and l[len(l)-1]!='1'):
    o+=1
   if(x=='10'):
    for i in l:
     if(i=='00' or i=='11'):
      v+=1
     elif(i=='10'):
      v+=2
    if(s[len(s)-1]!='0'):
     v+=1
   else:
    for i in l:
     if(i=='00' or i=='11'):
      v+=1
     elif(i=='01'):
      v+=2
    if(s[len(s)-1]!='1'):
     v+=1
  if(x=='01'):
   for i in l:
    if(i=='00' or i=='11'):
     o+=1
    elif(i=='10'):
     o+=2
  else:
   for i in l:
    if(i=='00' or i=='11'):
     o+=1
    elif(i=='01'):
     o+=2
  if(v==0 or o<v):
   return o 
  else:
   return v