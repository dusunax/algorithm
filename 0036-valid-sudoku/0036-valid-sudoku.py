class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = len(board)
        rows = [set() for _ in range(n)]
        cols = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        for i in range(n):
            for j in range(n):
                num = board[i][j]

                if num == '.':
                    continue
                
                if num in rows[i]:
                    return False
                rows[i].add(num)

                if num in cols[j]:
                    return False
                cols[j].add(num)
                
                box_index = (i // 3) * 3 + (j // 3)
                if num in boxes[box_index]:
                    return False
                boxes[box_index].add(num)

                print(boxes)
        return True
                    
