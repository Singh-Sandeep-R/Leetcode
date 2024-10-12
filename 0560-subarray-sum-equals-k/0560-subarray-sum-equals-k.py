class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        presum = 0
        trk = {}
        trk [0] =1
        for i in range(len(nums)):
            presum = presum+ nums[i]
            if ((presum-k) in trk) :
                count+=trk[presum-k]
            if presum in trk :
                trk[presum]=trk[presum]+1 
            else :
                trk[presum] = 1
        return count