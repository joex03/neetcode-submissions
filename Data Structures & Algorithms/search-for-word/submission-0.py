class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        visited=set()
        rows:int=len(board)
        cols:int=len(board[0])
        index:int=0
        result:bool

        def dfs(r,c,i):
            if r>=rows or c >=cols or r<0 or c<0 or board[r][c]!=word[i] or (r,c) in visited:
                return False
            if i==len(word)-1: #we found the word
                return True

            visited.add((r,c))

            result =dfs(r+1,c,i+1) or dfs(r-1,c,i+1) or dfs(r,c+1,i+1) or dfs(r,c-1,i+1)

            visited.remove((r,c))            

            return result            

        for i in range (rows):
            for j in range (cols):
                if dfs(i,j,index):
                    return True

        return False

                
        