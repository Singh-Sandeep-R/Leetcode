class Solution:
    def reverse(self, x: int) -> int:
        def rev_number(x):
            rev_num = 0
            while (x>0):
                last_di = x%10
                rev_num = rev_num*10+last_di
                x=x//10
            return rev_num

        if x<0 :
            x= x*(-1)
            rev_num = rev_number(x)
            rev_num = rev_num*(-1)
            if (rev_num<((-2)**31)):
                return 0
            else :
                return (rev_num)
        rev_num = rev_number(x)
        if (rev_num>((2**31)-1)):
            return 0
        else :
            return rev_num