class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        
# Below code might take space of (N)
        # count_dict = {}
        # for num in nums :
        #     if num in count_dict :
        #         count_dict[num]+=1
        #     else :
        #         count_dict[num] = 1
        # check = (len(nums)//3)
        # temp = []
        # for key,values in count_dict.items():
        #     if values > check :
        #         temp.append(key)
        # return temp
#optimize it for O(1):
        count1= 0
        count2 =0
        el1 = float('-inf')
        if len(nums)>1:
            el2 = float('inf')
        else :
            return (nums)
        check = len(nums)//3
        
        for num in nums:
            if ((count1==0) and (num!=el2)):
                count1 =1
                el1 = num
            elif ((count2==0) and (num!=el1)):
                count2=1
                el2 = num
            elif (num==el1):
                count1+=1
            elif (num==el2):
                count2+=1
            else :
                count1 =count1-1
                count2= count2-1
        temp = []
        count1 =0
        count2 =0
        for num in nums:
            if el1==num:
                count1+=1
            elif el2 ==num:
                count2+=1
        if count1>check:
            temp.append(el1)
        if count2>check:
            temp.append(el2)
        return (temp)