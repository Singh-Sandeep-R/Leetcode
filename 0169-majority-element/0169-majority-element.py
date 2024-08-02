class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ## moore's voting algorithm 
        count =1
        el = nums[0]
        n= len(nums)
        for i in range(1,n):
            if count==0:
                el = nums[i]
            if nums[i]==el:
                count+=1
            else :
                count-=1
            if (i==n-1) & (count!=0):
                el = el
        count_maj = 0
        for i in range(n):
            if nums[i]==el:
                count_maj+=1
        if count_maj > n//2:
            return el
                
        