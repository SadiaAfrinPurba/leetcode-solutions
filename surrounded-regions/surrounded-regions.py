from typing import List


class Solution:
    def flood_fill(self, board: List[List[str]], row: int, col: int,
                   row_dimension: int, col_dimension: int, old_color: str, new_color: str) -> None:
        if row < 0 or row >= row_dimension or col < 0 or col >= col_dimension:
            return

        if board[row][col] != old_color:
            return

        board[row][col] = new_color

        self.flood_fill(board, row + 1, col, row_dimension, col_dimension, old_color, new_color)
        self.flood_fill(board, row - 1, col, row_dimension, col_dimension, old_color, new_color)
        self.flood_fill(board, row, col + 1, row_dimension, col_dimension, old_color, new_color)
        self.flood_fill(board, row, col - 1, row_dimension, col_dimension, old_color, new_color)

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        row_dimension = len(board)
        col_dimension = len(board[0])

        for row in range(row_dimension):
            for col in range(col_dimension):
                if board[row][col] == 'O':
                    board[row][col] = '$'

        # TOP border
        for col in range(col_dimension):
            if board[0][col] == '$':
                self.flood_fill(board, 0, col, row_dimension, col_dimension, '$', 'O')

        # LEFT border
        for row in range(row_dimension):
            if board[row][0] == '$':
                self.flood_fill(board, row, 0, row_dimension, col_dimension, '$', 'O')

        # RIGHT border
        for row in range(row_dimension):
            if board[row][col_dimension - 1] == '$':
                self.flood_fill(board, row, col_dimension - 1, row_dimension, col_dimension, '$', 'O')

        # BOTTOM border
        for col in range(col_dimension):
            if board[row_dimension - 1][col] == '$':
                self.flood_fill(board, row_dimension - 1, col, row_dimension, col_dimension, '$', 'O')

        for row in range(row_dimension):
            for col in range(col_dimension):
                if board[row][col] == '$':
                    board[row][col] = 'X'



