class Solution:
    def totalNQueens(self, n: int) -> int:
        board = [[0]*n for _ in range(n)]
        return self.NQueens(board,0)
    
    def NQueens(self,board,row):
        if row == len(board):
            return 1
        
        count = 0

        for col in range(len(board[0])):
            if (self.isSafe(board,row,col)):
                board[row][col] = 1
                count = count + self.NQueens(board,row+1)
                board[row][col] = 0
        return count

    def isSafe(self,board,row,col):
        r = row
        c = col

        #Check vertically
        for r in range(row-1,-1,-1):
            if board[r][col] == 1:
                return False

        #Check PosDiag
        r = row - 1
        c = col - 1
        while r>=0 and c>=0:
            if board[r][c] == 1:
                return False
            r -= 1
            c -= 1
        
        #Check NegDiag
        r = row - 1
        c = col + 1
        while r>=0 and c<len(board):
            if board[r][c] == 1:
                return False
            r -= 1
            c += 1
        return True

        