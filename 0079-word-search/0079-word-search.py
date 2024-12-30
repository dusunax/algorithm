class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        
        def backtracking(i, j, word_index):
            if word_index == len(word):
                return True
            
            if i < 0 or i >= rows or j < 0 or j >= cols or board[i][j] != word[word_index]:
                return False
            
            temp_mark = board[i][j]
            board[i][j] = "."
            
            found = (
                backtracking(i + 1, j, word_index + 1) or
                backtracking(i - 1, j, word_index + 1) or
                backtracking(i, j + 1, word_index + 1) or
                backtracking(i, j - 1, word_index + 1)
            )
            
            board[i][j] = temp_mark
            
            return found
        
        for row in range(rows):
            for col in range(cols):
                if backtracking(row, col, 0):
                    return True
        
        return False
