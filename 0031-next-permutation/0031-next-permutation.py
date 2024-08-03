class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        overlap_ind = n-2
        while(overlap_ind>=0):
            if nums[overlap_ind]<nums[overlap_ind+1]:
                break
            else :
                overlap_ind -=1
        if overlap_ind ==-1 :
            nums[:] = nums[::-1]
            return
        swap_elem = nums[overlap_ind]
        for i in range(n-1,overlap_ind,-1):
            if (nums[i]>swap_elem) :
                # swap_elem = nums[i]
                next_min_index = i
                break
        nums[overlap_ind] = nums[next_min_index]
        nums[next_min_index] = swap_elem
        nums[overlap_ind+1:] = nums[overlap_ind+1:][::-1]
        return (nums)
            
            
                
        
        
        