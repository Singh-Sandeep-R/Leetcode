class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s)==1):
            return True
        s = s.lower()
        s = "".join(char for char in s if char.isalnum())
        s_rev = s[::-1]
        if s==s_rev:
            return True
        return False
        