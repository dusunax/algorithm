/**
 * @param {number} m
 * @param {number} n
 * @return {number}
 */
var uniquePaths = function(m, n) {
    const tails = new Array(m).fill(0).map(() => new Array(n).fill(0));
    for (let i = 0; i < m; i++) {
        tails[i][0] = 1;
    }
    for (let j = 0; j < n; j++) {
        tails[0][j] = 1;
    }

    tails[0][0] = 1;
    
    for (let k = 1; k < m; k++) {
        for (let l = 1; l < n; l++) {
            tails[k][l] = tails[k - 1][l] + tails[k][l - 1];
        }
    }
    
    return tails[m - 1][n - 1]
};