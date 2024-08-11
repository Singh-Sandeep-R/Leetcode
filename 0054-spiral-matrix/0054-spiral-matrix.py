class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top = left = 0
        right = len(matrix[0])-1
        bottom = len(matrix)-1
        spiral = []
        while((left<=right) & (top<=bottom)):
            for i in range(left,right+1):
                spiral.append(matrix[left][i])
            top +=1
            for i in range(top,bottom+1):
                spiral.append(matrix[i][right])
            right = right -1
            if (top<= bottom):
                for i in range(right,left-1,-1):
                    spiral.append(matrix[bottom][i])
                bottom = bottom -1
            if (right>=left):
                for i in range(bottom,top-1,-1):
                    spiral.append(matrix[i][left])
                left = left+1
        return spiral
        