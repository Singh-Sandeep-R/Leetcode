class Solution:
    def longestPalindrome(self, s: str) -> str:
        if (len(s)==0) or ((len(s)==2) and (s[0]==s[1])):
            return s
        if  (len(s)==1) or (len(s)==2):
            return s[0]
        dict_pal = {}
        for i in range(len(s)):
            start = i
            if s[start] in s[i+1:]:
                end_indices = [i for i,ch in enumerate(s) if ch==s[start]]
                end_indices.pop(0)
                for index in end_indices:
                    subs = s[start:index+1]
                    if subs==subs[::-1]:
                        dict_pal[subs]= len(subs)
        sort_dict = sorted(dict_pal.items(),key = lambda x : x[1], reverse = True)
        if sort_dict:
            return sort_dict[0][0]
        else:
            return s[0]



        