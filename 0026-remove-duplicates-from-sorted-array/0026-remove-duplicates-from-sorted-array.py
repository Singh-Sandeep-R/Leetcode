class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r =1
        n = len(nums)
        while((r>l) & (r<=n-1)):
            if nums[r]==nums[l]:
                nums[r:n-1] = nums[r+1:n]
                # nums[n-1] = -999
                n = n-1
                r=1
                l=0
            else:
                r= r+1
                l=l+1
        for j in range(len(nums)-1):
            if nums[j]==nums[j+1]:
                return j+1