class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        l,r = 0,0
        total,res = 0,0
        
        while r<len(nums):
            total = total+nums[r]
            
            while nums[r]*(r-l+1) > total+k :
                total-= nums[l]
                l=l+1
            res = max(res,r-l+1)
            r= r+1
        return res