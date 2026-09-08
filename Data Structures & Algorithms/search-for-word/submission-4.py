class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.wordPresent = False
        rows = len(board)
        cols = len(board[0])

        def backtrack(i, j, k):
            if k == len(word):
                self.wordPresent = True

            if not is_valid(i, j, k):
                return

            cacheChar = board[i][j]
            board[i][j] = None
            
            backtrack(i-1, j, k+1)
            backtrack(i+1, j, k+1)
            backtrack(i, j-1, k+1)
            backtrack(i, j+1, k+1)

            board[i][j] = cacheChar     

        def is_valid(i, j, k):   
            if (i < 0 
                or i >= rows 
                or j < 0 
                or j >= cols 
                or self.wordPresent
                or board[i][j] != word[k]):
                return False
            return True

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0]:
                    backtrack(i, j, 0)
        
        return self.wordPresent