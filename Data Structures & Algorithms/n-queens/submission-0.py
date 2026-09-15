class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.']*n for _ in range(n)]
        ans = []
        self.Nqueens(board,0,ans)
        return ans
    
    def printBoard(self,board,ans):
        sol = []
        for i in range(len(board)):
            sol.append("".join(board[i]))
        ans.append(sol)
        return ans

    def Nqueens(self,board,row,ans):
        if row == len(board):
            self.printBoard(board,ans)
            return

        for col in range(len(board[0])):
            if self.isSafe(board,row,col):
                board[row][col] = 'Q'
                self.Nqueens(board,row+1,ans)
                board[row][col] = '.'
    
    def isSafe(self,board,row,col):
        r = row
        c = col
        #Check vertically
        for r in range(row-1,-1,-1):
            if board[r][col] == 'Q':
                return False

        #Check PosDiag
        r = row-1
        c = col-1
        while r>=0 and c>=0:
            if board[r][c] == 'Q':
                return False
            r -= 1
            c -= 1
        
        #Check NegDiag
        r = row-1
        c = col+1
        while r>=0 and c<len(board):
            if board[r][c] == 'Q':
                return False
            r -= 1
            c += 1
            
        return True
            

        