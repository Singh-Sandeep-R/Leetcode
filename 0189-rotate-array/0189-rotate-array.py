class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        if n>1:
            k = k%n
            temp = nums[-k:]
            # print(temp)
            i=n-1-k
            if len(temp)<n:
                while(i>=0):
                    nums[i+k] =nums[i]
                    # print(f"for {i}th",a)
                    i=i-1
                nums[:k]= temp
                

        