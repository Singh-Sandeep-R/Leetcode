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
        return el
                
                
        