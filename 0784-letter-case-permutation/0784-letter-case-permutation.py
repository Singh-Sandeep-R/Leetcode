class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        s_out=''
        list_string=[]
        def solve1(s,s_out, list_string):
            if len(s)==0:
                list_string.append(s_out)
                # print(list_string)         
            else:
                if s[0].isalpha():
                    s_out1 = s_out+s[0].lower()
                    s_out2 = s_out + s[0].upper()
                    solve1(s[0+1:],s_out1,list_string)              
                    solve1(s[0+1:],s_out2,list_string)
                else:
                    s_out1 = s_out + s[0]
                    solve1(s[0+1:],s_out1,list_string)

        solve1(s,s_out,list_string)
        return(list_string)
        # print(list_string)

            