/**
 * @param {character[][]} board
 * @return {boolean}
 */
var isValidSudoku = function(board) {
    // check 
    // 1. row contain 1-9
    // 2. column contain 1-9
    // 3. 3 x 3 sub-boxes contain 1-9

    // use Hash Set
    const rows = new Array(9).fill(null).map(() => new Set());
    const cols = new Array(9).fill(null).map(() => new Set());
    const boxes = new Array(9).fill(null).map(() => new Set());

    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {
            const current = board[i][j];
            if (current === '.') continue;

            if (rows[i].has(current)) return false;
            rows[i].add(current);

            if (cols[j].has(current)) return false;
            cols[j].add(current);

            const boxIndex = Math.floor(i / 3) * 3 + Math.floor(j / 3);
            if (boxes[boxIndex].has(current)) return false;
            boxes[boxIndex].add(current);
        }
    }
    
    return true;
};
