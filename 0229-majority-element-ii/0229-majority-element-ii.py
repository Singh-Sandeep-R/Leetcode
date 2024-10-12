class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count_dict = {}
        for num in nums :
            if num in count_dict :
                count_dict[num]+=1
            else :
                count_dict[num] = 1
        check = (len(nums)//3)
        temp = []
        for key,values in count_dict.items():
            if values > check :
                temp.append(key)
        return temp