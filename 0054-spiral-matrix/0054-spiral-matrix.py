class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        def upper(spiral,matrix,r_s,c_s,r_e,c_e):
            row_list = [j for j in matrix[r_s][c_s:c_e]]
            col_list = []
            for i in range(r_s,r_e+1):
                if i<= r_e:
                    col_list.append(matrix[i][c_e])
        #     print("Upper_row",row_list)
        #     print("Upper_col",col_list)
            for el in row_list :
                spiral.append(el)
            for el in col_list :
                spiral.append(el)
            return spiral
        def lower (spiral,matrix,r_s,c_s,r_e,c_e):
            row_list = [j for j in matrix[r_e][c_s+1:c_e+1]]
            row_list = row_list[::-1]
            for el in row_list:
                spiral.append(el)
        #     print("lower_row",row_list)
            col_list = []
            for i in range(r_s,r_e+1):
                if i<= r_e:
                    col_list.append(matrix[i][c_s])
            col_list = col_list[::-1]
        #     print("lower_col",col_list)
            for el in col_list:
                spiral.append(el)

            return spiral
        r_s = 0
        c_s = 0
        r_e = len(matrix)-1
        c_e = len(matrix[0])-1
        spiral = []
        
        while((c_e>=c_s) & (r_e>=r_s)):
            spiral = upper(spiral,matrix,r_s,c_s,r_e,c_e)
            r_s+=1
            r_e = r_e
            c_e = c_e -1
        #     print(f"after {k}th Upper time",k)
        #     print(r_s,r_e,c_s,c_e)
            if ((c_e<c_s) | (r_e<r_s)):
                break
            spiral = lower(spiral,matrix,r_s,c_s,r_e,c_e)
            r_e = r_e-1 
        # #     c_e = c_e-1
            if r_s>0:
                c_s = c_s+1
        #     print(f"after {k}th down time",k)
        #     print(r_s,r_e,c_s,c_e)
        return spiral
        