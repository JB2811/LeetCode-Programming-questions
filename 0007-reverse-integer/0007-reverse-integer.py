import math
class Solution:
 z=pow(2,31)-1
 y=-1*z+1
 def reverse(self, x: int) -> int:
  c=0; d=0
  if(x<0):
   x=-1*x
   d+=1
  while(x!=0):
   c=(10*c+x%10) 
   x=math.floor(x/10)
  if(d>0):
   c=-1*c
  if(c>self.z or c<self.y):
   c=0
  return c