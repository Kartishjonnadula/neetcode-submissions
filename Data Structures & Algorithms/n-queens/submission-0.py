class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def isvalid(board,n,row,col):
            for i in range(len(board)):
                if board[row][i]=='Q':
                    return False
                if board[i][col]=='Q':
                    return False
            i,j=row,col
            i, j = row - 1, col - 1
            while i >= 0 and j >= 0:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j -= 1
            i, j = row - 1, col + 1
            while i >= 0 and j < n:
                if board[i][j] == 'Q':
                    return False
                i -= 1
                j += 1
            # board[row][col]="here"
            return True
        ans=[]
        def solve(n,row,board):
            if n==0:
                ans.append(["".join(r) for r in board])
                # ans.append(l)
                # print(board)
                return 
            for col in range(len(board)):
                if isvalid(board,len(board),row,col):
                    board[row][col]='Q'
                    solve(n-1,row+1,board)
                    board[row][col]='.'
        board=[["."]*n for i in range(n)]
        solve(n,0,board)
        return ans





