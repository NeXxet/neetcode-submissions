class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.wordPresent = False

        def backtrack(i, j, currentWord):
            if i < 0 or i >= len(board):
                return
            if j < 0 or j >= len(board[i]):
                return
            if board[i][j] == None or self.wordPresent:
                return

            cacheChar = board[i][j]
            currentWord = currentWord + cacheChar

            if currentWord == word:
                self.wordPresent = True

            board[i][j] = None

            backtrack(i-1, j, currentWord)
            backtrack(i+1, j, currentWord)
            backtrack(i, j-1, currentWord)
            backtrack(i, j+1, currentWord)

            board[i][j] = cacheChar        
            
        for i, row in enumerate(board):
            for j, col in enumerate(row):
                if col == word[0]:
                    backtrack(i, j, "")
        
        return self.wordPresent