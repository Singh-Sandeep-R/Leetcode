class Solution:
    def frequencySort(self, s: str) -> str:
        map_s = {char: s.count(char) for char in set(s)}
        map_s = sorted(map_s.items(), key= lambda x: x[1],reverse = True)
        return "".join(char*count for char,count in map_s)