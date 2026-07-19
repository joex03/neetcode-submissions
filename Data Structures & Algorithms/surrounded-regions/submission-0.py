class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows=len(board)
        cols=len(board[0])
        def helper(r,c):
            if r<0 or r>=rows or c<0 or c>=cols or board[r][c]!='O':
                return
            board[r][c]='T'
            helper(r,c-1)
            helper(r,c+1)
            helper(r-1,c)
            helper(r+1,c)
        for r in range(rows):
            if board[r][0]=='O':
                 helper(r,0)
            if board[r][cols-1]=='O':
                helper(r,cols-1)
        for c in range(cols):
            if board[0][c]=='O':
                helper(0,c)
            if board[rows-1][c]=='O':
                helper(rows-1,c)
        for r in range(rows):
            for c in range(cols):
                if board[r][c]=='O':
                    board[r][c]='X'
                if board[r][c]=='T':
                    board[r][c]='O'