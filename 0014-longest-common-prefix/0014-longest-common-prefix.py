class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        len_str = [len(str) for str in strs]
        min_p = min(len_str)
        if min_p==0:
            return ("")
        min_index = len_str.index(min_p)
        p =0
        # i = 0
        while(p<min_p):
            i = 0
            while(i<=len(strs)-2):
                if strs[i][p]==strs[i+1][p]:
                    i=i+1
                else:
                    return (strs[i][:p])
            p = p+1
        return (strs[min_index])