class Solution:
    def check(self, nums: List[int]) -> bool:
        c= 0
        n = len(nums)
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                c+=1
        if nums[n-1]>nums[0]:
            c+=1
        return c<=1
        