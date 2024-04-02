class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
     nums=nums1+nums2
     nums=sorted(nums)
     if(len(nums)%2!=0):
      return nums[int(len(nums)/2)]
     else:
      return float(nums[int(len(nums)/2)]+nums[int(len(nums)/2)-1])/2.0
        