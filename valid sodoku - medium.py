"""
Determine if a 9 x 9 Sudoku board is valid. 
Only the filled cells need to be validated according to the following rules:
1. Each row must contain the digits 1-9 without repetition.
2. Each column must contain the digits 1-9 without repetition.
3. Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

Note:
· A Sudoku board (partially filled) could be valid but is not necessarily solvable.
· Only the filled cells need to be validated according to the mentioned rules.
"""

def valid_sudoku(board):
    def is_valid_block(block):
        nums = [num for num in block if num != '.']
        return len(nums) == len(set(nums))

    for row in board:
        if not is_valid_block(row):
            return False

    for col in range(9):
        if not is_valid_block([board[row][col] for row in range(9)]):
            return False

    for box_row in range(3):
        for box_col in range(3):
            block = []
            for i in range(3):
                for j in range(3):
                    block.append(board[box_row * 3 + i][box_col * 3 + j])
            if not is_valid_block(block):
                return False

    return True

#yeah i got no clue.
