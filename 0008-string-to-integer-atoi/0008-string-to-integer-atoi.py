class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        if len(s)==0:
            return 0
        sign = 1
        if s[0] in ["-"]:
            sign = -1
            s = s[1:]
        elif s[0] in ["+"]:
            sign = 1
            s = s[1:]
        if s and (s[0] in ["-","+"]):
            return 0
        result = ""
        for char in s:
            if char.isdigit():
                result += char
            else:
                break
        if result=="":
            return 0
        num = sign*int(result)
        INT_MIN, INT_MAX = -2**31, 2**31 - 1
        num = max(INT_MIN, min(INT_MAX, num))
        return num
        