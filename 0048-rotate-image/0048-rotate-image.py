class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        from copy import deepcopy
        """
        Do not return anything, modify matrix in-place instead.
        """
        matrix_1 = deepcopy(matrix)
        n = len(matrix_1)
        for i in range(len(matrix[0])):
            for j in range(len(matrix)):
                matrix[j][i] = matrix_1[n-i-1][j]
                # print(matrix)
        # print(matrix)
                
        