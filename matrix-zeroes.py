class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        row = set()
        col = set()
        rl = len(matrix)
        cl = len(matrix[0])
        for i in range(rl):
            for j in range(cl):
                if(matrix[i][j] == 0):
                    row.add(i)
                    col.add(j)
        for i in range(rl):
            for j in range(cl):
                if i in row or j in col:
                    matrix[i][j] = 0