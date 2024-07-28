class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        trk_frqn = {}
        n = len(nums)
        
        for elem in nums :
            if elem not in trk_frqn :
                trk_frqn[elem] = 1
            else :
                trk_frqn[elem] +=1
        # print(trk_frqn)
        for k, v in trk_frqn.items() :
            if v==1:
                return k