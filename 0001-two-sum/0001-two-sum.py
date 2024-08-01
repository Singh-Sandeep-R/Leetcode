class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        trk ={}
        result =[]
        for i in range(len(nums)):
            if (target-nums[i]) not in trk.keys():
                trk[nums[i]] = i
            else :
                result.append(i)
                result.append(trk[target-nums[i]])
                break
        return (result)
                
        