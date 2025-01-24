class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
      
        zero_rows = set()
        zero_cols = set()

        for r in range(len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    zero_rows.add(r)
                    zero_cols.add(c)

        for r in zero_rows:
            for i in range(len(matrix[0])):
                matrix[r][i] = 0

        for c in zero_cols:
            for i in range(len(matrix)):
                matrix[i][c] = 0