class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        n= len(nums)
        result = 0
        for i in range (n-2):
            if ((nums[i]<nums[i+1]) & (nums[i+2]<nums[i+1])):
                if nums[result]<nums[i+1]:
                    result = i+1
            
        if (nums[n-2]<nums[n-1]) & (nums[n-1]>nums[0]):
            if nums[result] < nums[n-1]:
                result = n-1
        return result
            
        