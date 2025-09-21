class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        n1 = len(s)
        n2 = len(t)
        if n1!=n2:
            return False
        dict_check_s = {}
        dict_check_t = {}
        for i in range(n1):
            if (s[i] not in dict_check_s):
                dict_check_s[s[i]]= t[i]
            else :
                if dict_check_s[s[i]]!=t[i]:
                    return False
            if (t[i] not in dict_check_t):
                dict_check_t[t[i]]= s[i]
            else :
                if dict_check_t[t[i]]!=s[i]:
                    return False
        return True


        