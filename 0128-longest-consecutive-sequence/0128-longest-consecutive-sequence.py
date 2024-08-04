class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        result = 1
        count = 1
        min_ele = nums[0]
        for i in range(len(nums)):
            if nums[i]==min_ele:
                pass
            elif nums[i]-min_ele==1:
                min_ele = nums[i]
                count = count+1
                result = max(result,count)
            else :
                min_ele = nums[i]
                count = 1
        return(result)
                
                
            
        
        