class Solution {
    private String word;
    private int rows;
    private int cols;
    private char[][] board;
    
    public boolean exist(char[][] board, String word) {
        this.rows = board.length;   
        this.cols = board[0].length;
        this.word = word;
        this.board = board;

        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < cols; j++) {
                if (board[i][j] == word.charAt(0)) {
                    if (backtracking(i, j, 0)) {
                        return true;
                    }
                }
            }
        }
        return false;
    }
    public boolean backtracking(int i, int j, int wordIndex) {
        if (wordIndex == word.length()) return true;
        if (
            i < 0 || 
            i >= rows || 
            j < 0 || 
            j >= cols || 
            board[i][j] != word.charAt(wordIndex)
        ) return false; 
        

        char temp = board[i][j];
        board[i][j] = '.';
    
        boolean found = (
            backtracking(i + 1, j, wordIndex + 1) ||
            backtracking(i - 1, j, wordIndex + 1) ||
            backtracking(i, j + 1, wordIndex + 1) ||
            backtracking(i, j - 1, wordIndex + 1)
        );

        board[i][j] = temp;
        return found;
    }
}
