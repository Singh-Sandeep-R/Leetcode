class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        pascal = []
        pascal.append([1])
        if numRows>=2:
            pascal.append([1,1])
        for row in range(3,numRows+1) :
            temp =[]
            for col in range(row):
                if col==0:
                    ans = 1
                else :
                    ans = ans*(row-col)
                    ans = ans/col

                temp.append(int(ans))
            pascal.append(temp)
        return pascal
                
            
        