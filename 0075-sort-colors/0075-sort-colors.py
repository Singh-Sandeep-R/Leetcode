class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        for i in range(n):
            j=i
            while ((j>0) & (nums[j-1]>nums[j])):
                temp = nums[j-1]
                nums[j-1] = nums[j]
                nums[j] = temp
                j= j-1
                
        