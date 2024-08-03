class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ### Brute Force
#         pos_list = []
#         neg_list = []
#         res_list = []
#         i= 0
#         while(i<len(nums)):
#             if nums[i]>0:
#                 pos_list.append(nums[i])
#             else :
#                 neg_list.append(nums[i])
#             i=i+1
#         # print(pos_list)
#         # print(neg_list)
#         p = 0
#         n = 0
#         for i in range(len(nums)):
#             if i%2==0:
#                 res_list.append(pos_list[i-n])
#                 p = p+1
#             else :
#                 res_list.append(neg_list[i-p])
#                 n= n+1
        

#         return res_list
####### Optimal Solution #########
        p = 0
        n = 0
        res_list = [0]*len(nums)
        for i in range(len(nums)):
            if nums[i]>0:
                res_list[2*p] = nums[i]
                p= p+1
            else :
                res_list[2*n+1] = nums[i]
                n = n+1

        return(res_list)

        
        