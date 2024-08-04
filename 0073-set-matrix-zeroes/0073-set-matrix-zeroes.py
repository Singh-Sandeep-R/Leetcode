class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row = []
        col = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                if matrix[i][j]==0:
                    if i not in row:
                        row.append(i)
                    if j not in col :
                        col.append(j)
        row_pointer = 0
        col_pointer = 0
        while(row_pointer<len(row)):
            for j in range(len(matrix[0])):
                matrix[row[row_pointer]][j] = 0
            row_pointer+=1
        while((col_pointer<len(col))):
            for i in range(len(matrix)):
                matrix[i][col[col_pointer]] = 0
            col_pointer +=1
        return matrix
            
        