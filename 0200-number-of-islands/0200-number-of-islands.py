class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or y >= len(grid) or x >= len(grid[0]) or grid[y][x] == "0" :
                return
            print(x, y, grid[y][x])
        
            grid[y][x] = "0"
            dfs(x, y + 1)
            dfs(x - 1, y)
            dfs(x, y - 1)
            dfs(x + 1, y)
        
        island_count = 0
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                if grid[y][x] == "1":
                    dfs(x, y)
                    island_count += 1
        
        print(grid)

        return island_count

        