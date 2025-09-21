class Solution:
    def frequencySort(self, s: str) -> str:
        map_s = {char: s.count(char) for char in set(s)}
        map_s = sorted(map_s.items(), key= lambda x: x[1],reverse = True)
        final_string = ""
        for tuples in map_s:
            final_string += tuples[0]*tuples[1]
        return final_string