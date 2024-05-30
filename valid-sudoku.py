class Solution(object):
    def isValidSudoku(self, board):
        row = [[] for _ in range(9)]
        column = [[] for _ in range(9)]
        dic = [[] for _ in range(9)]
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n!='.':
                    index = (i // 3) * 3 + (j // 3)
                    if n in column or n in row or n in dic[index]:
                        return False
                    row[i].append(n)
                    column[j].append(n)
                    dic[index].append(n)
                    print(dic)
                
                
        return True
        
        
print(Solution.isValidSudoku(0, [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]))