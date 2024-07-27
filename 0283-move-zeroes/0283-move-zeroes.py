class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        c= 0
        for i in range(len(nums)):
            if 0 in nums :
                nums.remove(0)
                c+=1
        for j in range(c):
            nums.append(0)