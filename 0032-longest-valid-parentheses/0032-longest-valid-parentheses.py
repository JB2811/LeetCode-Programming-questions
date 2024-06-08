class Solution:
 def longestValidParentheses(self, s: str) -> int:
  i=0;
  s=list(s)
  while(i<len(s)):
   if(s[i]!=')'):
    i+=1
   else:
    i-=1
    while(i>=0 and s[i]!='('):
     i-=1
    if(i>=0 ):
     s[i]='x'
     while(s[i]!=')'):
      i+=1;
     s[i]='x'
    else:
     i+=1
     while(s[i]!=')'):
      i+=1;
     s[i]='y'
    i+=1;
  c=0;
  t=0;
  i=0;
  while(i<len(s)):
   if(s[i]=='x'):
    c+=1
   else:
    if(c>=t):
     t=c
    c=0
   i+=1;
  if(c>t):
   t=c
  print(s)
  return t 