import copy
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        n1=sorted(nums)
        n2=copy.deepcopy(n1)
        n2.reverse()
        print(n1," ",n2)
        if(n1==nums or nums==n2):
            return True
        else:
            return False