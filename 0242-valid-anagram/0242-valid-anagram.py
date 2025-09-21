class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        map_s = {}
        map_t  = {}
        count = 0
        for i in range(len(s)):
            if s[i] not in map_s:
                map_s[s[i]] = 0
            else:
                map_s[s[i]]+=1
            if t[i] not in map_t:
                map_t[t[i]] = 0
            else:
                map_t[t[i]]+=1
        return (map_t==map_s)


        