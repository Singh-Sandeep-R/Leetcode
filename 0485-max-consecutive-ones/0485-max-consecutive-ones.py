class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        var_count = 0
        maxim=0
        n = len(nums)
        for i in range(n):
            if nums[i]==1:
                var_count+=1
            else :
                var_count=0
            print(var_count)
            maxim = max(maxim,var_count)
        return maxim
            
        