class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def sink(grid, i, j):
            if i<0 or j<0 or i>=len(grid) or j>=len(grid[0]) or grid[i][j] == '0':
                return
            grid[i][j] = '0'
            sink(grid,i+1,j)
            sink(grid,i-1,j)
            sink(grid,i,j+1)
            sink(grid,i,j-1)

        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == '1':
                    count += 1 
                    sink(grid,i,j)

        return count