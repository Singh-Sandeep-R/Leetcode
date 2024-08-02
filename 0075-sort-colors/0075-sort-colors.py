class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        ### Dutch National Flag Algorithm
        n = len(nums)
        mid = 0
        left = 0
        high = n-1
        while(mid<=high):
            if nums[mid]==0:
                temp = nums[mid]
                nums[mid] = nums[left]
                nums[left] = temp
                mid+=1
                left+=1
            elif nums[mid]==1:
                mid+=1
            else :
                temp = nums[mid]
                nums[mid] = nums[high]
                nums[high] = temp
                high -=1
                
                
                
        