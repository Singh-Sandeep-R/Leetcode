class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        trk = {}
        for elem in nums :
            if elem not in trk :
                trk[elem] = 1
            else :
                trk[elem]+=1
        for k, v in trk.items():
            if v>(len(nums)//2):
                return k
        