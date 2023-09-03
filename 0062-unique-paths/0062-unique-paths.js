/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const tiles = new Array(m).fill(0).map(() => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        tiles[i][0] = 1;
    }
    for (let j = 0; j < n; j++) {
        tiles[0][j] = 1;
    }
    
    for (let k = 1; k < m; k++) {
        for (let l = 1; l < n; l++) {
            tiles[k][l] = tiles[k - 1][l] + tiles[k][l - 1];
        }
    }
    
    return tiles[m - 1][n - 1]
};