class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums.sort()
        result = 1
        # result1 = 0
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return 1
        count = 1
        min_ele = nums[0]
        
        for i in range(len(nums)):
            if nums[i]==min_ele:
                pass
            elif nums[i]-min_ele==1:
                # print(i)
                min_ele = nums[i]
                count = count+1
                result = max(result,count)
            else :
                print(i)
                min_ele = nums[i]
                count = 1
                print(min_ele)
        return(result)
                
                
            
        
        