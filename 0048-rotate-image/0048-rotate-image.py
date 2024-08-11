class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        i = 0
        while(i<=n):
            j=i+1
            while((j<n) & (i<j)):
                temp = matrix[i][j]
                matrix[i][j] = matrix[j][i]
                matrix[j][i] = temp
                j+=1
            i+=1
        for i in range(n):
            matrix[i] = matrix[i][::-1]
                
        