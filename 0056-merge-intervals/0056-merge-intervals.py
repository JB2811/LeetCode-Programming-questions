class Solution:
 def merge(self, intervals: List[List[int]]) -> List[List[int]]:
  c=1
  for i in range(0,len(intervals)):
   for j in range(i+1,len(intervals)):
    if intervals[i][0]>intervals[j][0]:
     t=intervals[i]
     intervals[i]=intervals[j]
     intervals[j]=t
  while(c):
   c=0
   for i in range(0,len(intervals)):
    for j in range(i+1,len(intervals)):
     if j<len(intervals) and intervals[i][1]>=intervals[j][0]:
      intervals.insert(i,[min(intervals[i][0],intervals[j][0]),max(intervals[j][1],intervals[i][1])])
      intervals.pop(i+1)
      intervals.pop(j)
      c=1
  return intervals