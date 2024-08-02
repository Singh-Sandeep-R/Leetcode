class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # count = 0 
        # l = 0
        # r = len(nums)-1
        # while(l<=r):
        #     if nums[l] == val:
        #         if nums[r]!= val :
        #             temp = nums[l]
        #             nums[l] =nums[r]
        #             nums[r] = temp
        #             l=l+1
        #             r=r-1
        #             # count +=1
        #         else:
        #             r=r-1
        #     else :
        #         l=l+1
        # for i in range(len(nums)):
        #     if nums[i]==val:
        #         count +=1
        # return count
        
        c= 0
        for i in range(len(nums)):
            if nums[i]==val :
                nums[i] = 0
                c=c+1
        l = len(nums)
        nums.sort(reverse=True)
        return (l-c)
            
            
        
    
        