from copy import deepcopy

class edge:
 def __init__(self,s,d):
  self.source=s
  self.dest=d
  self.dist=sum([abs(s[0]-d[0]),abs(s[1]-d[1])])

class Solution:
 
 def minCostConnectPoints(self, points: List[List[int]]) -> int:
  
  n=len(points)

  if(n<2):
   return 0
    
  edges=[]
    
  for i in range(n):
   points[i]=tuple(points[i])

  for i in range(0,n):
   for j in range(i+1,n):
    if(points[i]!=points[j]):
     e=edge(points[i],points[j])
     edges.append(deepcopy(e))

  covered=dict.fromkeys(points,1)
  reachable=dict.fromkeys(points,[])

  for i in points:
   reachable[i]=[i]
    
  s=0;j=0
  while(1):
   m=100000000000000000000000
   for i in edges:
    if(i.dist<m and (i.dest not in reachable[i.source])):
     m=i.dist
     e=i
   s+=m
    
   edges.remove(e) 
   reachable[e.source]=list(set(reachable[e.source]+reachable[e.dest]))
   reachable[e.dest]=reachable[e.source]
   
   if(len(reachable[e.source])==n):
     return s
    
   for i in reachable[e.source]:
    reachable[i]=reachable[e.source]
  
  
 
