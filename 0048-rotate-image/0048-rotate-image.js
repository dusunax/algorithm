/**
 * @param {number[][]} matrix
 * @return {void} Do not return anything, modify matrix in-place instead.
 */
// matrix rotation
// by Transpose + Reverse
// in-place 90도 회전 알고리즘
var rotate = function (matrix) {
  const n = matrix.length;

  for (let i = 0; i < n; i++) {
    for (let j = i; j < n; j++) {
      [matrix[i][j], matrix[j][i]] = [matrix[j][i], matrix[i][j]]; // 행렬의 행(row)과 열(column)을 서로 교환
    }
  }

  for (let i = 0; i < n; i++) {
    matrix[i].reverse(); // 행렬의 각 행을 역순으로 바꿈
  }
};