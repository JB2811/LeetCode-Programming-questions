import copy
class Solution:
    def sortColors(self, nums: List[int]) -> None:
     c=[]
     for i in range(3):
      c.append(0)
     d=copy.deepcopy(nums)
     for i in nums:
      c[i]+=1
     for i in range(1,3):
      c[i]=c[i]+c[i-1]
     for i in range(3):
      if(c[i]>0):
       c[i]-=1    
     for i in range(len(d)): 
      nums[c[d[i]]]=d[i]
      c[d[i]]-=1
        