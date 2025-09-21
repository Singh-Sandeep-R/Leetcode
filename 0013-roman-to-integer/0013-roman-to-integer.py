class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {"I":1,
         "V":5,
         "X":10,
         "L":50,
         "C":100,
         "D":500,
         "M":1000}
        count = 0
        point = 0
        while (point<len(s)):
            print(point)
            if (point<len(s)-1) and (roman[s[point]]>=roman[s[point+1]]):
                count += roman[s[point]]
                point = point+1
            elif (point==len(s)-1):
                count+=roman[s[point]]
                break 

            else :
                count = count + roman[s[point+1]]-roman[s[point]]
                point = point+2
        return count
        
        