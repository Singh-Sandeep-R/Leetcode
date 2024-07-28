class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n =len(nums)
        sum = (n*(n+1))/2
        sum1= 0
        for i in range(n):
            sum1=sum1+nums[i]
        return int(abs(sum-sum1))