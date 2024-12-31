/**
 * @param {character[][]} board
 * @param {string} word
 * @return {boolean}
 */
var exist = function(board, word) {
    const rows = board.length;
    const cols = board[0].length;
    let wordIndex = 0;
    
    const backtracking = (i, j, wordIndex) => {
        if (wordIndex === word.length) return true;
        if (
            i < 0 ||
            i >= rows ||
            j < 0 ||
            j >= cols ||
            board[i][j] !== word[wordIndex]
        ) return false;

        const temp = board[i][j];
        board[i][j] = '.';
        
        const found = (
            backtracking(i + 1, j, wordIndex + 1) ||
            backtracking(i - 1, j, wordIndex + 1) ||
            backtracking(i, j + 1, wordIndex + 1) ||
            backtracking(i, j - 1, wordIndex + 1)
        )

        board[i][j] = temp;
        return found;
    }

    for (let i = 0; i < rows; i++){
        for(let j = 0; j < cols; j++){
            if (board[i][j] === word[0]) {
                if(backtracking(i, j, 0)){
                    return true;
                }
            }
        }
    }

    return false;
};