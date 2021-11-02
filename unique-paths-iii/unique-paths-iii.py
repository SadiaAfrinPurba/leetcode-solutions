class Solution:
    
    def uniquePathsIII(self, obstacleGrid: List[List[int]]) -> int:
        row_dimension = len(obstacleGrid)
        col_dimension = len(obstacleGrid[0])
        
        num_empty_cell, start_row, start_col, end_row, end_col = 1, 0, 0, 0, 0
        
        self.num_of_path = 0
        
        for row in range(row_dimension):
            for col in range(col_dimension):
                if obstacleGrid[row][col] == 1:
                    start_row, start_col = row, col
                
                elif obstacleGrid[row][col] == 2:
                    end_row, end_col = row, col
                
                elif obstacleGrid[row][col] == 0:
                    num_empty_cell += 1
        
        visited = set()
        
        def dfs(row: int, col: int, visited: set, path: int) -> int:
            if row == end_row and col == end_col:
                if num_empty_cell == path:
                    self.num_of_path += 1
                return
            
            if 0 <= row < row_dimension and 0 <= col < col_dimension and obstacleGrid[row][col] != -1 and (row, col) not in visited:
                
                visited.add((row, col))
                
                dfs(row + 1, col, visited, path + 1)
                dfs(row - 1, col, visited, path + 1)
                dfs(row, col + 1, visited, path + 1)
                dfs(row, col - 1, visited, path + 1)
            

                visited.remove((row, col))
                
        dfs(start_row, start_col, visited, 0)
        
        return self.num_of_path


                


        